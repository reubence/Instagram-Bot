<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Last Commit][last-activity-shield]][last-activity-url] <br />
[![LinkedIn][linkedin-shield]][linkedin-url]
<!--[![MIT License][license-shield]][license-url]-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/reubence/Instagram-Bot">
    <img src="https://pythonawesome.com/content/images/2018/08/Followers-on-Instagram.jpg" alt="Logo" >
  </a>

  <h3 align="center">Instagram Bot</h3>

  <p align="center">
    An automated bot which looks for memes on <a href = "reddit.com">Reddit<a/> and uploads them on instagram without human intervention.
    <!--<br />
    <a href="https://github.com/reubence/Instagram-Bot"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
    <a href="https://price-tracker-abgb.herokuapp.com/">View Demo</a>
    ·
    <a href="https://github.com/reubence/Instagram-Bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/reubence/Instagram-Bot/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About this Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)<!--* [Prerequisites](#prerequisites)  * [Installation](#installation)-->
* [Usage](#usage)<!--* [Roadmap](#roadmap)-->
* [Contributing](#contributing)<!--* [License](#license)-->
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project
<p align="center">
  <a href="https://price-tracker-abgb.herokuapp.com/">
    <img src="dataset/img.png" alt="Logo" >
  </a>
 <h5 align="center">A Snapshot of the web-app</h5>
  <p align="center">


There are many great toold available on the internet to track prices of big e-commerce sites such as Amazon or Flipkart, however, I didn't find one that was configured to track prices of PrimeABGB; an Indian vendor that sells computer parts and other electronics stores across India. 

Hence, I created this very basic price tracker app to help me track the prices of multiple products which I was planning on purchasing. This web-app helped me to catch some ongoing discounts, which I would've otherwise missed. In the end I saved approximately 10,000 INR :smile:.

Of course this oversimplified version of the app will not serve all of you, since your needs may be different. So I'll be adding more features in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue.

### Built With

* [Heroku](https://heroku.com/)
* [Dash](https://plotly.com/dash/)



<!-- GETTING STARTED -->
## Getting Started
First things first, this project is configured to track very few products which you may/may not be looking to buy. So you'll have to tinker a bit with the code to add your products to the list in order to start tracking them.
### Prerequisites

Before we begin, you need a couple of things installed...
* Download and Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and type the following to log into your heroku account ```heroku login ```. 
* Download and Install [git](https://git-scm.com/downloads)
* ``` pip install requirements.txt```

<!-- USAGE EXAMPLES -->
## Usage

1. Fork This Repo, and clone it locally using git.
2. In the dataset folder and change the ***Links.csv*** file by replacing the URL's in it with your own product URLs taken from PrimeABGB's website. 
3. Follow the usual steps for deployment to heroku and deploy your version of the app. It should be able to tell you the prices in one page.

Now you can visit the deployed app anytime during and check prices of all products at a glance.

You could go further and use the Gmail API to configure the app to send a message as the prices fall down below a certain level.

<!-- ROADMAP 
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).

-->

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be, learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE` for more information.
-->


<!-- CONTACT -->
## Contact

Reuben Rapose - [LinkedIn](https://www.linkedin.com/in/reubence/) - reuben.rapose@gmail.com

Project Link: [https://github.com/reubence/Prime-ABGB-Custom-Price-Tracker](https://github.com/reubence/Prime-ABGB-Custom-Price-Tracker)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Heroku](https://heroku.com/)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
<!--* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)-->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[last-activity-shield]: https://img.shields.io/github/last-commit/reubence/Instagram-Bot?style=flat-square
[last-activity-url]: https://github.com/reubence
[contributors-shield]: https://img.shields.io/github/contributors/reubence/Instagram-Bot.svg?style=flat-square
[contributors-url]: https://github.com/reubence
[forks-shield]: https://img.shields.io/github/forks/reubence/Instagram-Bot.svg?style=flat-square
[forks-url]: https://github.com/reubence/Instagram-Bot/network/members
[stars-shield]: https://img.shields.io/github/stars/reubence/Instagram-Bot.svg?style=flat-square
[stars-url]: https://github.com/reubence/heroku-template/stargazers
[issues-shield]: https://img.shields.io/github/issues/reubence/Instagram-Bot.svg?style=flat-square
[issues-url]: https://github.com/reubence/heroku-template/issues
[license-shield]: https://img.shields.io/github/license/reubence/Instagram-Bot.svg?style=flat-square
[license-url]: https://github.com/reubence/Instagram-Bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/reubence/
[product-screenshot]: https://lh3.googleusercontent.com/proxy/l3Fi5jqPd6axyq2qRIgC_LqGaQgY4TplQuqMBctQlzhH2wEidEIbA2BNpVOrSC7idwzDB6G_pm-tLvZMbJa6BVznty5hQH7XlSWe4XjbHO_tAgO7H7o4-3IUERI6Kqgs