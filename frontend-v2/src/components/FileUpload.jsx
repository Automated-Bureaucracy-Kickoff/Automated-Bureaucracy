import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';
import AddIcon from '@mui/icons-material/Add';
import { useDispatch } from 'react-redux';
import { appendFiles } from '../redux/slices/chatbotState';


const VisuallyHiddenInput = styled('input')({
  clip: 'rect(0 0 0 0)',
  clipPath: 'inset(50%)',
  height: 1,
  overflow: 'hidden',
  position: 'absolute',
  bottom: 0,
  left: 0,
  whiteSpace: 'nowrap',
  width: 1,
});

export default function FileUpload() {
    const dispatch = useDispatch()
  return (
    <Button
      component="label"
      role={undefined}
       color='whitesmoke'    
      tabIndex={-1}
      startIcon={<AddIcon />}
      className='absolute -left-8'
      
    >
      <VisuallyHiddenInput
        type="file"
        onChange={(event) => dispatch(appendFiles({files:event.target.files}))  }
        multiple
      />
    </Button>
  );
}
