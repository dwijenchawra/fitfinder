import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView, Button, Image } from 'react-native';
import { useEffect, useRef, useState } from 'react';
import { Camera } from 'expo-camera';
import * as ImagePicker from 'expo-image-picker'

export default function CameraSection() {
  let cameraRef = useRef();
  const [hasCameraPermission, setHasCameraPermission] = useState();
  const [photo, setPhoto] = useState();

  useEffect(() => {
    (async () => {
      const cameraPermission = await Camera.requestCameraPermissionsAsync();
      setHasCameraPermission(cameraPermission.status === "granted");
    })();
  }, []);

  if (hasCameraPermission === undefined) {
    return <Text>Requesting permissions...</Text>
  } else if (!hasCameraPermission) {
    return <Text>Permission for camera not granted. Please change this in settings.</Text>
  }

  async function takeAndUploadPhotoAsync() {
    let result = await ImagePicker.launchCameraAsync({
      allowsEditing: true,
      aspect: [4, 3],
    });
  
    if (result.cancelled) {
      return;
    }
  
    let localUri = result.uri;
    let filename = localUri.split('/').pop();
    let match = /\.(\w+)$/.exec(filename);
    let type = match ? `image/${match[1]}` : `image`;

    let formData = new FormData();
    formData.append('image', { uri: localUri, name: filename, type });

    return await fetch("http://23.119.122.47:5000/process", {
      method: 'POST',
      body: formData,
      headers: {
        'content-type': 'multipart/form-data',
      },
    });
  }

  async function pingServer() {
    const req = new XMLHttpRequest();
    req.open("GET", "http://23.119.122.47:5000");
    req.send();
    console.log("request sent")
  }


  return (
    <View style={styles.container}>
      <Button
        onPress={takeAndUploadPhotoAsync}
        title="Capture a new piece of clothing"
        color="#841584"
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  buttonContainer: {
    backgroundColor: '#fff',
    alignSelf: 'flex-end'
  },
  preview: {
    alignSelf: 'stretch',
    flex: 1
  }
});