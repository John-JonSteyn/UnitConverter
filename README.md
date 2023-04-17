<div id="top"></div>
<div align="center">

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- Title -->
<br />
  <h3 align="center">Unit Converter - A Terminal-based Unit Converter</h3>
  
  <hr>
  
  <p align="center">
    Funcion-heavy and simplistic unit converter for distances, masses, temperatures and time conversions. 
    <br />
    <a href="https://github.com/Bearded-Viking/UnitConverter/"><strong>View Source Code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Bearded-Viking/UnitConverter/issues">Report Bug</a>
    ·
    <a href="https://github.com/Bearded-Viking/UnitConverter/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#the-basics-of-unitconverter">The Basics of the Unit Converter</a></li>
    <ul>
        <li><a href="#main-menu">Main Menu</a></li>
        <li><a href="#distance">Distance</a></li>
        <li><a href="#mass">Mass</a></li>
        <li><a href="#temperature">Temperature</a></li>
        <li><a href="#time">Time</a></li>
        <li><a href="#speed">Speed</a></li>
        <li><a href="#quit">Quit</a></li>
    </ul>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Annoyed with your Canadian cousins' celcius? Frustrated with your British friends refering to distances as miles that aren't "Morales"? Ever tried convert between the metric and imperial systems by hand?

Well now you don't have to. This simple script will do it for you. We've got your back, so that you can go back to the fun life with less measurement politics and less math.

There are many unit converters available on GitHub - probably more than I can count; however, this is mine. Created without guides, nor based on templates - this "bush code", albeit rudamentary and primitave, demonstrates the practicality of functions, elif and the metric system.

Unit Converter supports the following Units of Meassurement:
1. Distance
  * Kilometer (km)
  * Meter (m)
  * Centimeter (cm)
  * Millimeter (mm)
  * Miles (mi)
  * Yards (yd)
  * Inches (in)
2. Mass
  * Tonnes (t)
  * Kilogram (kg)
  * Gram (g)
  * Milligram (mm)
  * Pounds (lbs)
  * Stone (st)
  * Ounces (oz)
3. Temperature
  * Degrees Celcius (C)
  * Kelvin (K)
  * Degrees Farenheit (F)
  * Degrees Rankine (R)
4. Time
  * Days (d)
  * Hours (hr)
  * Minutes (min)
  * Seconds (sec)
5. Speed
  * Mile Per Hour (mph)
  * Kilometers Per Hour (kph)
  * Meters Per Second (mps)
  * Knots (kt)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python 3.10.4](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Setting up Unit Converter on your local machine is as simple as 1, 2, 3. Just follow the steps; 1, 2 and 3.

### Prerequisites

You'll need Python 3.8 or higher. Don't worry, it doesn't bite ... often.

How to download the lastest version of Python:
* Click [here](https://www.python.org/downloads/) to navigate to python's official page.
* Click on the big, flashy "Download Python [version]" button.
* Save the executable file.
* Open the .exe file within the downloaded location, and follow the installation instructions.


### Installation

1 Open the terminal / command prompt:
  * On PC: Open Command prompt by pressing start, then typing "cmd" then hit ENTER.
  * On Mac OS: Click the Launchpad icon in the Dock, type Terminal in the search field, then click Terminal.

2. Navigate to the directory you would like to install Unit Converter:
  ```sh
  cd [DirectoryPathHere]
  ```
3. Clone the repository by entering the following command into your shell:
   ```sh
   git clone https://github.com/Bearded-Viking/UnitConverter.git
   ```
It's that simple! You can run Unit converter with following command:

  ```sh
  python unitconverter.py 
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## The Basics of Unit Converter

[![Unit Converter Main][screenshot-main]]((https://github.com/Bearded-Viking/UnitConverter/blob/main/images/screenshotMain.png))
When you run the script, this message will be displayed. From here we can select which dimention we would like to convert in.

### Distance
To select Distance, we'll just type it out:
  ```sh
  Distance
  ```

[![Distance Enter Value][screenshot-distance-enter-value]]((https://github.com/Bearded-Viking/UnitConverter/blob/main/images/screenshotDistanceEnterValue.png))

Now we select a unit we'd like to convert from, for example:
  ```sh
  Meter
  ```

[![Distance Select][screenshot-distance-select]]((https://github.com/Bearded-Viking/UnitConverter/blob/main/images/screenshotDistanceSelect.png))
Next enter the value of our unit, for illustation
  ```sh
  273
  ```

[![Distance Output][screenshot-distance-output]]((https://github.com/Bearded-Viking/UnitConverter/blob/main/images/screenshotDistanceOutput.png))

Now we have our measurement converted and returned to us in each of the units.
We are also sent back to the main menu.

### Mass
Mass follows the same logic, as can be seen here:
[![Mass][screenshot-mass]]((https://github.com/Bearded-Viking/UnitConverter/blob/main/images/screenshotMass.png))

### Temperature
As is the case with Temperature:
[![Temperature][screenshot-temperature]]((https://github.com/Bearded-Viking/UnitConverter/blob/main/images/screenshotTemperature.png))

### Time
And, not surprisingly, Time is no different:
[![Time][screenshot-time]]((https://github.com/Bearded-Viking/UnitConverter/blob/main/images/screenshotTime.png))

### Speed
Same with speed. Who would've thought:
\<Insert Screenshot here\>

### Quit
You can also quit the program at any time by typing:
  ```sh
  Quit
  ```
[![Quit][screenshot-quit]]((https://github.com/Bearded-Viking/UnitConverter/blob/main/images/screenshotQuit.png))

<!-- ROADMAP -->
## Roadmap

- [x] "Kilometre" changed to "Kilometer"
- [x] Fixed Temperature-function call
- [x] Revised system exit
- [x] Add back to top links
- [x] Remove Case-Sensitivity
- [ ] Improve Output Appearance
- [ ] Add option to utilise acronyms as input

See the [open issues](https://github.com/Bearded-Viking/UnitConverter/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
I'd like to thank Nikolai, who not only supported me in my endevour to start loading my projects onto GitHub, but also helped fuzzing and de-bugging my first program.
* [Nikolai James Manilal](https://github.com/NikhirMG)

I'd also like to acknowledge and recommend these resources that made the learning python even simpler than it already is.
* [Geeks for Geeks](https://www.geeksforgeeks.org/)
* [Zurik Phillips](https://github.com/zuriknet/README)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Bearded-Viking/UnitConverter.svg?style=for-the-badge
[contributors-url]: https://github.com/Bearded-Viking/UnitConverter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Bearded-Viking/UnitConverter.svg?style=for-the-badge
[forks-url]: https://github.com/Bearded-Viking/UnitConverter/network/members
[stars-shield]: https://img.shields.io/github/stars/Bearded-Viking/UnitConverter.svg?style=for-the-badge
[stars-url]: https://github.com/Bearded-Viking/UnitConverter/stargazers
[issues-shield]: https://img.shields.io/github/issues/Bearded-Viking/UnitConverter.svg?style=for-the-badge
[issues-url]: https://github.com/Bearded-Viking/UnitConverter/issues
[license-shield]: https://img.shields.io/github/license/Bearded-Viking/TaskFlow.svg?style=for-the-badge
[license-url]: https://github.com/Bearded-Viking/UnitConverter/blob/master/LICENSE.txt

[screenshot-distance-enter-value]: images/screenshotDistanceEnterValue.png
[screenshot-distance-output]:images/screenshotDistanceOutput.png
[screenshot-distance-select]:images/screenshotDistanceSelect.png
[screenshot-main]:images/screenshotMain.png
[screenshot-mass]:images/screenshotMass.png
[screenshot-quit]:images/screenshotQuit.png
[screenshot-temperature]:images/screenshotTemperature.png
[screenshot-time]:images/screenshotTime.png 
