import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Slide from '@mui/material/Slide';
import { TextField } from '@mui/material';
import { useDispatch } from 'react-redux';
import { createTitle } from '../redux/slices/chatbotState';

const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});

export default function ChangeTitle({setChangetitle}) {
  const [open, setOpen] = React.useState(true);
    const dispatch = useDispatch()
    
  const handleClose = () => {
    dispatch(createTitle(document.getElementById("standard-basic").value));
    setOpen(false);
    setChangetitle(false)
  };

  return (
    <React.Fragment>
      <Dialog
        open={open}
        TransitionComponent={Transition}
        keepMounted
        onClose={handleClose}
        aria-describedby="alert-dialog-slide-description"
        sx={{
            ".MuiPaper-root": {
              width: "80vw",
              padding: "19px",
              borderRadius: "12px",
              backgroundColor: "var(--color-primary-bg)",
              color: "var(--color-primary-text)"
            },
            ".MuiDialogTitle-root": {
              color: "var(--color-primary-text)"
            },
            ".MuiTextField-root": {
              input: { color: "var(--color-primary-text)" },
              label: { color: "var(--color-secondary-text)" }
            },
            ".MuiButton-root": {
              color: "var(--color-primary-text)"
            }
          }}
      >
        <DialogTitle >{"Change your Chat Title ?"}</DialogTitle>
        <TextField id="standard-basic" label="Title" variant="standard"  />

        <DialogActions>
          <Button onClick={handleClose}>Close</Button>
          <Button onClick={handleClose}>Change</Button>
        </DialogActions>
      </Dialog>
    </React.Fragment>
  );
}