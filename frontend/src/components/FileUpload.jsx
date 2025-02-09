import AddIcon from "@mui/icons-material/Add";
import { useDispatch } from "react-redux";
import { appendFiles } from "../redux/slices/chatbotState";
import {  useState } from "react";

import { CircularProgress } from '@mui/material';

export default function FileUpload() {
  const dispatch = useDispatch();
  const [isUploading, setIsUploading] = useState(true);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setIsUploading(false);
      setTimeout(() => {
        setIsUploading(true);
        dispatch(appendFiles({ files: event.target.files }));
      }, 1500);
    }
  };

  return (
    <div className="relative">
      {isUploading ? 
        <>
          <input
            type="file"
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
            onChange={(event) => handleFileChange(event)}
            multiple
          />

          <div className="flex justify-center items-center bg-gray-400 hover:bg-gray-300 p-3 rounded-full transition cursor-pointer w-10 h-10">
            <AddIcon className="text-black" />
          </div>
        </>
        : <CircularProgress className="relative -left-14 -top-[0.75px]" />
      }
    </div>

  );
}