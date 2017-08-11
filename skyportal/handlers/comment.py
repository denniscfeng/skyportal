import tornado.web
from baselayer.app.access import permissions
from baselayer.app.handlers.base import BaseHandler
from ..models import DBSession, Source, User, Comment, Role


class SourceCommentsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, source_id):
        results = (DBSession
                   .query(Comment, User.username)
                   .join(User)
                   .filter(Comment.source_id == source_id))
        comments = [
            {**comment.to_dict(), 'username': username}
            for (comment, username) in results
        ]

        return self.success(data=comments)


class CommentHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, comment_id):
        # TODO: Ensure that it's okay for anyone to read any comment
        comment = Comment.query.get(comment_id)
        return self.success(data=comment)

    @permissions(['Comment'])
    def post(self):
        data = self.get_json()
        source_id = data['source_id'];

        comment = Comment(user=self.current_user,
                          text=data['text'], source_id=source_id)

        DBSession().add(comment)
        DBSession().commit()

        return self.success(action='skyportal/FETCH_COMMENTS',
                            payload={'source_id': source_id})

    @permissions(['Comment'])
    def put(self, comment_id):
        data = self.get_json()

        # TODO: Check ownership
        c = Comment.query.get(comment_id)
        c.text = data['text']

        DBSession().commit()

        return self.success(action='skyportal/FETCH_COMMENTS',
                            payload={'source_id': c.source_id})

    @permissions(['Comment'])
    def delete(self, comment_id):
        # TODO: Check ownership
        c = Comment.query.get(comment_id)
        DBSession().delete(c)
        DBSession().commit()

        return self.success(action='skyportal/FETCH_COMMENTS',
                            payload={'source_id': c.source_id})