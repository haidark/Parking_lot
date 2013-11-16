N02062147
=========

Parking lot occupancy measurement using image processing

For a detailed guide on how to use this software, read "https://github.com/haidark/N02062147/blob/master/docs/index.html"

Goal of the project:

-Given static video footage of an aerial view of a parking lot;
	Determine the number and locations of unoccupied parking spots
	Determine the number and locations of occupied parking spots

Approach:

- Given static video footage of an aerial view of a parking lot.
- Determine each parking spots location
	Use user-labeled ROI's to localize each parking spot
	(A GUI will be provided to get this information easily and save it)
- Then, use one of the following technique to decide whether a parking spot is occupied or not
	1. Template matching - localized image subtraction
	2. Canny Edge detection
	3. Histogram of Oreinted Gradients
- Once the ROI is converted to one of these three forms, compare it to the parking spot when it is unoccupied
- Finally, report the status of each spot


Progress:

9/3/13 - Project start

9/6/13 - Researched related work

9/10/13 - Formulated basic approach

10/3/13 - Create Github Repository

11/3/13 - Created basic framework (mid-way)

11/12/13 - Created documentation

11/14/13 - Created ROI extraction function - getROI.py
			generates file ROIs.txt containing user specified ROIS

11/16/13 - Create ROI comparison function - loadROI.py
			get templates specified by ROIs.txt
			gets a video of parking lot
			compares template to ROI in current frame of video
			determines state of parkinglot
			only done for 1 so far
			currently using simple image subtraction
			TO DO: use Canny edge or HOG or SIFT





