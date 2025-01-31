import AddIcon from "@mui/icons-material/Add";
import { useDispatch } from "react-redux";
import { appendFiles } from "../redux/slices/chatbotState";

export default function FileUpload() {
  const dispatch = useDispatch();

  return (
    <div className="relative">
      {/* Hidden File Input */}
      <input
        type="file"
        className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
        onChange={(event) => dispatch(appendFiles({ files: event.target.files }))}
        multiple
      />

      {/* Circular Upload Button */}
      <div className="flex justify-center items-center bg-gray-400 hover:bg-gray-300 p-3 rounded-full transition cursor-pointer w-10 h-10">
        <AddIcon className="text-black" />
      </div>
    </div>
  );
}
