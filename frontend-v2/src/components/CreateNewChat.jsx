import { Button } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import SettingsIcon from "@mui/icons-material/Settings";
import { useDispatch } from "react-redux";
import { createHistory } from "../redux/slices/chatbotState";
import { toggleSetting } from "../redux/slices/settings";

function CreateNewChat() {
  const dispatch = useDispatch();

  function clearChat() {
    dispatch(createHistory());
  }

  return (
    <div className="flex justify-between items-center px-4 mt-4">
      <Button
        onClick={clearChat}
        className="text-white capitalize"
        startIcon={<AddIcon />}
      >
        Create New Chat
      </Button>
      <SettingsIcon
        onClick={() => dispatch(toggleSetting())}
        className="hover:animate-spin cursor-pointer"
      />
    </div>
  );
}

export default CreateNewChat;
