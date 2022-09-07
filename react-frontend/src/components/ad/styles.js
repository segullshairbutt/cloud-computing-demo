import { makeStyles } from '@mui/styles';
import { generalStyles } from '../../generalStyles';

const useStyles = makeStyles(theme => ({
    adContainer: {
        display: 'flex',
        flexDirection: 'row',
        marginTop: '1rem',
        marginBottom: '1rem',
    },
    imageContainer: {
        width: '20%',
        height: '220px',
        borderRadius: '5px',
        boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)',
        marginRight: '5%',
    },
    image: {
        width: '100%',
        height: '100%',
        objectFit: 'cover',
        borderRadius: '5px',
    },
    mediaInfoContainer: {
        width: '70%',
    },
    mediaHeading: {
        fontFamily: generalStyles.openSans,
        color: '#5A5A5A',
        fontWeight: '600',
        fontSize: '2rem',
        margin: 0,
        padding: 0,
    },
    mediaDescription: {
        fontFamily: generalStyles.openSans,
        color: '#838381',
        fontSize: '1rem',
        margin: 0,
        padding: 0,
        marginTop: '0.5rem'
    },
    mediaType: {
        fontFamily: generalStyles.openSans,
        color: '#5A5A5A',
        fontSize: '1.25rem',
        margin: 0,
        padding: 0,
        marginTop: '0.5rem',
        fontWeight: 500,
    },
    mediaPrice: {
        fontFamily: generalStyles.openSans,
        color: '#5A5A5A',
        fontSize: '1.25rem',
        margin: 0,
        padding: 0,
        marginTop: '0.5rem',
        fontWeight: 500,
    },
    uploadModalContainer: {
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'center', 
    },
    box: { 
        display: 'flex',
        flexDirection: 'column',
        width: '40%',
        maxHeight: '80vh',
        borderRadius: '10px',
        backgroundColor: '#FAF9F6',
        border: '2px solid grey',
        overflowX: 'hidden',
        paddingBottom: '2%'
    },
    box1: { 
        display: 'flex', 
        flexDirection: 'column',
        width: '100%',
        padding: '0 2rem',
    },
    inputContainer: { 
        display: 'flex', 
        flexDirection: 'row', 
        justifyContent: 'space-between', 
        alignItems: 'center', 
        marginBottom: '3%'
    },
    buttonsContainer: {
        display: 'flex', 
        flexDirection: 'row', 
        justifyContent: 'space-around',
    },
    boxHeading: {
        fontSize: '1.25rem',
        fontFamily: "Open Sans",
        fontWeight: '600',
        color: 'white',
        margin: '0.5rem 0',
        padding: 0
    },
    boxHeader: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'center',
        alignContent: 'center',
        borderTopLeftRadius: '10px',
        borderTopRightRadius: '10px',
        marginBottom: '3%',
        backgroundColor: generalStyles.primaryColor
    },
}))

export default useStyles