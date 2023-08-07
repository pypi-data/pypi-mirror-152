DIR="edgeapps"
if [ -d "$DIR" ]; then
  # Take action if $DIR exists. #
  echo "deleting the cloned repository"
  sudo rm -rf $DIR
  if ! [[ -d "$DIR" ]]; then
          echo "Repository removed sucessfully"
  fi
else
  echo "Repository does not exist to delete"
fi

