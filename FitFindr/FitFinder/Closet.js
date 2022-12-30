import React, { useState } from 'react';
import { View, Image, StyleSheet, Text, SafeAreaView, ScrollView, StatusBar } from 'react-native';

const Closet = () => {


  return (
    <SafeAreaView style={styles.container}>
      <ScrollView style={styles.scrollView}>
        <Text style={styles.clothingContainer}>Tops</Text>
        <ScrollView style={styles.scrollView} horizontal={true}>
            <View style={styles.image}>
                <Image source={require('./assets/clothes_Home.jpeg')}/>
                <Text style={styles.textContainer}>Black Jacket</Text>
            </View>
        </ScrollView>
        <Text style={styles.clothingContainer}>Bottoms</Text>
        <ScrollView style={styles.scrollView} horizontal={true}>
            <View style={styles.image}>
                <Image source={require('./assets/clothes_Home.jpeg')}/>
                <Text style={styles.textContainer}>Black Pants</Text>
            </View>
        </ScrollView>
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

export default Closet;