import { useNavigation } from "@react-navigation/native";
import React from "react";
import { Button } from "@react-native-material/core";
import { Image, ImageBackground, StyleSheet, Text, View } from "react-native";

const Home = () => {
  const navigation = useNavigation();
  return (
    <View style={styles.container}>
      <View style={styles.group}>
        <ImageBackground
          source={require("./assets/clothes_Home.jpeg")}
          resizeMode="contain"
          style={styles.image}
          imageStyle={styles.image_imageStyle}
        >
          <View style={styles.rect2Stack}>
            <View style={styles.rect2}></View>
            <View style={styles.rect}></View>
          </View>
        </ImageBackground>
      </View>
      <Text style={styles.fitFinder}>Fit Finder</Text>
      <Button
      title="Add"
      onPress={() => navigation.navigate("camera")}
        style={styles.materialButtonViolet}
      ></Button>
      <Button
        title="Closet"
        style={styles.materialButtonViolet1}
        onPress={() => navigation.navigate("closet")}
      ></Button>
      <Button
        title="Make Fit"
        style={styles.materialButtonViolet2}
        onPress={() => navigation.navigate("makeFit")}
      ></Button>
      <Text style={styles.loremIpsum}>
        Welcome to Your Personal Wardrobe Stylist
      </Text>
    </View>
  );
} 

const styles = StyleSheet.create({
  container: {
    flex: 1
  },
  group: {
    width: 397,
    height: 200,
    marginTop: 150,
    marginLeft: 11
  },
  image: {
    width: 744,
    height: 870,
    marginTop: -90,
    marginLeft: -82
  },
  image_imageStyle: {},
  rect2: {
    top: -1,
    left: 1,
    width: 402,
    height: 90,
    position: "absolute",
    backgroundColor: "rgba(241,241,242,255)",
    transform: [
      {
        rotate: "-11.00deg"
      }
    ]
  },
  rect: {
    top: 80,
    left: 0,
    height: 8,
    position: "absolute",
    backgroundColor: "rgba(244,67,54,1)",
    borderRadius: 100,
    borderWidth: 0,
    borderColor: "#000000",
    transform: [
      {
        rotate: "-11.00deg"
      }
    ],
    width: 420
  },
  rect2Stack: {
    width: 425,
    height: 50,
    marginTop: 150,
    marginLeft: 65
  },
  materialButtonViolet: {
    height: 36,
    width: 142,
    borderWidth: 1,
    borderColor: "rgba(255,255,255,1)",
    borderRadius: 10,
    backgroundColor: "rgba(74,74,74,1)",
    opacity: 0.9,
    marginTop: 320,
    marginLeft: 117
  },
  materialButtonViolet1: {
    height: 35,
    width: 142,
    backgroundColor: "rgba(74,74,74,1)",
    borderWidth: 1,
    borderColor: "rgba(255,255,255,1)",
    borderRadius: 10,
    opacity: 0.9,
    marginTop: 34,
    marginLeft: 117
  },
  materialButtonViolet2: {
    height: 35,
    width: 142,
    borderWidth: 1,
    borderColor: "rgba(255,255,255,1)",
    backgroundColor: "rgba(74,74,74,1)",
    borderRadius: 10,
    opacity: 0.9,
    marginTop: 35,
    marginLeft: 117
  },
  fitFinder: {
    //fontFamily: "monospace",
    color: "#121212",
    fontSize: 40,
    marginTop: -259,
    alignSelf: "center"
  },
  loremIpsum: {
    //fontFamily: "monospace",
    color: "#121212",
    marginTop: -464,
    marginLeft: 10,
    alignSelf: "center"
  }
});

export default Home;