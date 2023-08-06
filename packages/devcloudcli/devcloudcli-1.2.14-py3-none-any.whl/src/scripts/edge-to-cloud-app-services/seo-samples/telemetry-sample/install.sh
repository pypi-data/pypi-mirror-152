#Checking if the git is present or not
if [[ $(which git) && $(git --version) ]]; then
        true
else
        echo "Git is not installed..Installing Git"
        sudo apt-get update
        sudo apt-get install git
fi

DIR="edgeapps"
if [ -d "$DIR" ]; then
  # Take action if $DIR exists. #
  echo "Repository already present"
else
  echo "Cloning the git repository"
  git clone https://github.com/smart-edge-open/edgeapps.git
  success=$?
  if [[ $success -eq 0 ]];then
    echo "Repository successfully cloned.."
    echo "Please navaigate to edgeapps/applications/telemetry-sample-app/"
  else
    echo "Something went wrong!"
  fi
fi
