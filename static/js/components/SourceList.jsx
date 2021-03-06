import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

import SearchBox from '../containers/SearchBox';


const SourceList = ({ sources }) => (
  <div>
    <h2>
      Sources
    </h2>

    <SearchBox sources={sources} />
    {
      !sources.queryInProgress &&
      <table id="tab">
        <thead>
          <tr>
            <th />
            <th />
            <th colSpan="2">
              Position
            </th>
            <th colSpan="4">
              Type
            </th>
            <th colSpan="2">
              Gaia
            </th>
            <th />
            <th />
            <th />
            <th />
          </tr>

          <tr>
            <th>
              Last detected
            </th>
            <th>
              Name
            </th>
            <th>
              RA
            </th>
            <th>
              DEC
            </th>
            <th>
              varstar
            </th>
            <th>
              transient
            </th>
            <th>
              disagree
            </th>
            <th>
              is_roid
            </th>
            <th>
              Gmag
            </th>
            <th>
              T<sub>eff</sub>
            </th>
            <th>
              Score
            </th>
            <th>
              N<br />detections
            </th>
            <th>
              Simbad <br />Class
            </th>
            <th>
              TNS Name
            </th>
          </tr>
        </thead>
        <tbody>
          {
            sources.latest && sources.latest.map((source, idx) => (
              <tr key={source.id}>
                <td>{source.last_detected && String(source.last_detected).split(".")[0]}&nbsp;&nbsp;</td>
                <td>
                  <Link to={`/source/${source.id}`}>
                    {source.id}
                  </Link>
                </td>
                <td>{source.ra && Number(source.ra).toFixed(3)}</td>
                <td>{source.dec && Number(source.dec.toFixed(4))}</td>
                <td>{source.varstar.toString()}</td>
                <td>{source.transient.toString()}</td>
                <td>{(source.transient == source.varstar).toString()}</td>
                <td>{source.is_roid.toString()}</td>
                <td>{source.gaia_info && Number(JSON.parse(source.gaia_info)["Gmag"]).toFixed(2)}</td>
                <td>{source.gaia_info && JSON.parse(source.gaia_info)["Teff"] && Number(JSON.parse(source.gaia_info)["Teff"]).toFixed(1)}</td>
                <td>{Number(source.score).toFixed(2)}</td>
                <td>{source.detect_photometry_count}</td>
                <td>{source.simbad_class}</td>
                <td>{source.tns_name}</td>
              </tr>
            ))
          }
        </tbody>
      </table>
    }
    {
      sources.queryInProgress &&
      <div><br /><br /><i>Query in progress...</i></div>
    }
  </div>
);

SourceList.propTypes = {
  sources: PropTypes.object.isRequired
};


export default SourceList;
