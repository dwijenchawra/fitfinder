import React, { useState } from 'react';
import { View, Image, StyleSheet, Text, SafeAreaView, ScrollView, StatusBar } from 'react-native';

const Fit = () => {


  return (
    <SafeAreaView style={styles.container}>
      <ScrollView style={styles.scrollView}>
        <Image source={require('./assets/istockphoto-163208487-612x612.jpeg')}/>
        <Text style={styles.textContainer}>Red Jacket</Text>
        <Image source={require('./assets/hmgoepprod.webp')}/>
        <Text style={styles.textContainer}>Black Pants</Text>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      paddingTop: StatusBar.currentHeight,
    },
    clothingContainer: {
        padding: 10,
        fontSize: 30,
        textAlign: 'center',
        alignItems: 'center',
        justifyContent: 'center',
    },
    image: {
        padding: 5
    },
    textContainer: {
        flex: 1,
        padding: 10,
        textAlign: 'center',
        alignItems: 'center',
        justifyContent: 'center',
    },
    scrollView: {
      marginHorizontal: 20,
    },
    text: {
      fontSize: 42,
    },
    
  });

export default Fit;