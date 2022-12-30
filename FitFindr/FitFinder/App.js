import React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import CameraSection from './takePicture.js';
import Home from './Home.js';
import Closet from './Closet.js';
import Fit from './Fit.js'


const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{headerShown: false}}>
        <Stack.Screen name="home" component={Home} />
        <Stack.Screen name="camera" component={CameraSection}/>
        <Stack.Screen name="closet" component={Closet}/>
        <Stack.Screen name="makeFit" component={Fit}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;