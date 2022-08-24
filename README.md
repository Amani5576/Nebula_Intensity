# Nebula Intensity

Analysing areas of high and low intensity of Statue of Liberty Nebulae based on user specifications.

Data sourced from [this site](https://www.mattdieterich.com/nebuladata "www.mattdieterich.com")  where it was captured from ObsTech in Chile.

## FitExtraction file (by Amani5576)
This file opens and extracts the HDU data from the fit files and puts them into an array; HDUs.
Each fit File consists of a Primary and an Image HDU. These are two sub-lists within each element of HDUs

`HDUs[0]` ---> `[PrimaryHDU, ImageHDU]` from Hydrogen Alpha Fit file
 
`HDUs[1]` ---> `[PrimaryHDU, ImageHDU]` from Oxygen III Fit file

`HDUs[2]` ---> `[PrimaryHDU, ImageHDU]` from Silicon II Fit file
     
Hence accessing the `ImageHDU` of in row element `x` of `HDUs` array: 
            
    HDUs[x][1]

Running the file allows you to get necessary information from the header of the Primary such as :


## DataAnalysis.py file (by Amani5576)
This file:
* Closes the Fit files that were opened in the FitsExtraction.py

* Takes the Image HDU data of fit files and puts them in numpy arrays

* Computes Statistical data with regards to pixel numbered values
    - Median pixel value
    - Mode(s) of pixel value(s)
    - Standard Deviation of pixel values.
    
* Allows user input in assesment of relative intenisty based on a specific ImageHDU

    -Lets user decide on scaling Factor. For Example:

         You've chosen Scaling factor to be 6 (6 levels of varying intensity):
         
         If max = 80 and min = 20 then range is (80 - 20) = 60
         By dividing the range by the Scale we get -> 60/6 = 10.
         Hence, from Level 1 (highest intensity) to Level 2
         (Second highest intensity) is a difference of 10.
     
    -Lets user decide on the number of level intensities desirable (from highest intesity as the first level)
    For Example:

        Level 1 -> highest intensity level (Thus, type in the integer "1")
        Level 2 -> 2nd highest intensity up until highest intenisty (Thus, type in the integer "2")
        Level 3 -> 3rd highest intensity up until highest intenisty (Thus, type in the integer "3")
        Level 4 -> 4th highest.......etc   
            
**NOTE**: There automatically exists an initial **level 0**. This intenisty level is only for one value in particular which has the highest intensity value within the *entire matrix*.
             
*The above essestially decreases processing time if not all intensity levels are desired.*

* Allows user to choose three data ouputs: (which are limited by users chosen Scaling factor)
    -Get pixels that belong to all levels of intensity up until the lowest intensity
    -Get pixels that belong to a particular level of intenisty 
    -Let pixels that belong to particular levels of intenisty 
        
The pixels will be given in terms of a tuple:

    (<x-coord> , <y-coord> , <Intensity_level>)

See image below with an example of chosen user input:

* Scaling Factor = `40`
* Level Limit = `10`
* Last user input = `Yes` *(in order to see all levels)*


Tuples are used further on in plotting of filtered data in spectra.py @rofhima13

For the Hydrogen Alpha Filtered data:

<img src="./img/TupleHA.jpeg">
    
For the Oxygen III Filtered data:

<img src="./img/TupleO3.jpeg">
    
For the Silicon II Filtered data:

<img src="./img/TupleS2.jpeg">


## showSection.py file (by Amani5576)
This file shows the initial image matrix of Hydrogen Alpha, Oxygen 3 and Silicon 2 data.

This is due to the fact that each numbered value in the matrices is a quanitity of the number of photons captured by the Telescope. Each element is a pixel containing a specified number of photons.

NOTE: Run seperately **AFTER** running through Data Analysis

In the command line, input:
    
    show(x)
    
where `x` is the name of the fits file (with extension **.fit**) in quotation.

Very useful for comparison between plots that are made with *spectra.py* file @rofhima13.

## spectra.py file (by rofhima13)

This file extracts the original image matrices, and filtered image matrices from the DataAnalysis module @Amani5576 constructed from the FIT files, and constructs a horizontal spectrum relative to the x-axis of the image, or from a viewer's point of view, and displays all of the resultant plots using all of the data.

For the purposes of demonstration, only information pertaining to the Hydrogen Alpha spectra will be shown below.

This is what the original Hydrogen Alpha image looks like:

<img src="./img/HA_full_image.png">

The full spectrum for the Hydrogen Alpha Nebula looks something like this:

<img src="./img/HA_full_spectrum.png">

When an image is constructed using the filtered data for the Hydrogen Alpha Nebula, it looks something like this (a different color filter is used):

<img src="./img/HA_filtered_image.png">

When the below spectrum for the filtered data is compared with the filtered image, it becomes easier to discern where the brightest spots in the image are located.

<img src="./img/HA_filtered_spectrum.png">

Taking note of all the above information, looking at the filtered spectrum it's evident that the brightest spots of the Hydrogen Alpha Nebula are located by the horizontal center of the image, and the filtered image reflects that information.

The file can be run by running ```python ./spectra.py``` on any terminal emulator on a computer with Python 3 installed.

Make sure to run ```pip install -r requirements.txt``` before you run!