import React from 'react'
import { downloadMedia } from '../../services/download'
import useStyles from './styles'
import Chip from '@mui/material/Chip';
import PlacehoderImage from "./../../assests/placeholder.png";


function AdminMedia(props) {
  const { name, description, cost, owner, date, is_approved, attachments, id, updateMediaStatus, mediaItem } = props
  const approveStatus = is_approved
  const classes = useStyles();
  return (
    <div className={classes.mainContainer}>
      <div className={classes.adContainer}>
        <div className={classes.imageContainer}>
          <img
            className={classes.image}
            src={`${(attachments && attachments.length !== 0 && attachments[0].url !== '') ? attachments[0].url : PlacehoderImage}`}
            alt="Media pic not found"
          />
        </div>
        <div className={classes.mediaInfoContainer}>
          <p className={classes.mediaHeading}>{name}</p>
          <p className={classes.mediaDescription}>{description}</p>
          <p className={classes.mediaPrice}>Cost: {cost}</p>
          <p className={classes.mediaPrice}>Owner: {owner}</p>
          <p className={classes.mediaPrice}>Uploaded on: {date}</p>
          <div style={{ display: 'flex', flexDirection: 'row', marginTop: '3%' }}>
          <p className={classes.mediaPrice}>Status:
            {
            approveStatus
              ?
              <Chip label={'Approved'} sx={{ marginLeft: '1%' }} color="success" />
              :
              <Chip label={'Not Approved'} sx={{ marginLeft: '1%' }} color="warning" />
            }
          </p>
            {
              approveStatus
                ?
                <button
                  className={classes.disapproveButton}
                  onClick={() => updateMediaStatus({
                    "ids": [id],
                    "approve": false
                  })}
                >
                  Disapprove
                </button>
                :
                <button
                  className={classes.approveButton}
                  onClick={() => updateMediaStatus({
                    "ids": [id],
                    "approve": true
                  })}
                >
                  Approve
                </button>
            }
            <button type="submit" disabled={false} onClick={() => downloadMedia(mediaItem)} className={classes.approveButton}>Download Media</button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default AdminMedia 	