# Mood Music Matcher Python Command Line App

This repository holds the code for a music mood matcher written in python using APIs availabe on [Public APIs](https://github.com/public-apis/public-apis). The application is designed for python command line only and lacks of any UI.

## Table of Contents

- [App setup and run](#app-development-and-run)
  - [1. Introduction](#1.-introduction)
  - [2. Install dependencies](#2.-install-dependencies)
  - [3. Setup env variables](#3.-setup-env-variables)
  - [4. Run](#4.-run)
    - [Functional programming](#functional-programming)
    - [Object oriented programming](#object-oriented-programming)
- [APIs](#apis)
- [Notes](#note)

## App setup and run

### 1. Introduction

This app aims to suggest the user a song based on their current feeling.

The user is asked to describe their feeling with a few words and then the user's input is sent to [Sentim-API](https://sentim-api.herokuapp.com/) (a machine learning sentiment analysis API) which analyses the feeling and returns feeling's polarity in terms of degree (a value between 0 and 1) and type (e.g. positive, negetive, neutral).

The user's input is validated with [detectlangauge](https://detectlanguage.com/) API which only allows the user to enter meaningful english sentences.

To find a suitable music, firstly, a keyword is created based on the user's feeling polarity and then the keyword is searched on [iTunes Search](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) API. This API returns a list of 50 songs which match the keyword.

One song is randomly chosen from the list and [Lyrics.ovh](http://docs.lyricsovh.apiary.io/) API is used to find lyrics for the song.

Finaly, the details of the song is displayed to the user.

### 2. Install dependencies

Apart from python built in libraries, there are three more libraries which you need to install. To install the dependencies, navigate to the root of the app and run `pip install -r requirements.txt`.

### 3. Setup env variables

In this app [detectlangauge](https://detectlanguage.com/) library has been used which requires api key for authentication. In oder to run the app, you need to get a free api and then, in the root directory of the app, create a _.env_ file and add your detectlanguage api key similar to _.env.example_ model.

### 4. Run

This app has been developed in both functional programming and object oriented programming.

#### programming

To run the functional app, navigate to the root of the app and run `python main_functional.py`

#### Object oriented programming

To run the object oriented app, navigate to the root of the app and run `python main_class.py`

## APIs

- [Sentim-API](https://sentim-api.herokuapp.com/) a Text sentiment analysis API
- [iTunes Search](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) iTune products search API
- [Lyrics.ovh](http://docs.lyricsovh.apiary.io/) a aimple API to retrieve the lyrics of a song
- [Detect Langauge](https://detectlanguage.com/) a text language detection API

## Notes

[Sentim-API](https://sentim-api.herokuapp.com/) is currently down. Therefore, for testing purposes, `mock_sentiment_request` function was developed for this API which is currently in use. This `mock_sentiment_request` function generates feeling's polarities with random values for type and degree. To use the actual request function, navigate to `sourceful` directory under the app root directory and in `api_modules.py` file, you can change the API request function for `analyse_feeling_polarity`.
