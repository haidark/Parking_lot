N02062147
=========

Parking lot occupancy measurement using image processing

Work I have done so far:

I have read into two papers regarding parking lot occupancy using image processions

- the first is by two malaysian students, I did not find this one helpful
- the second is called COINS, I found this one helpful but not exactly what i have in mind
- I am trying to obtain the full text of one more paper that I think will give me more insight

What I think my approach will be:

- Given static video footage of an aerial view of a parking lot.
- Use one of two approaches to determine occupancy
	1. use preset ROI's to localize each parking spot
	2. use some image processing technique to localize each parking spot
- Then, use one of the following technique to decide whether a parking spot is occupied or not
	1. Template matching - localized image subtraction
	2. Canny Edge detection
	3. Histogram of Oreinted Gradients
- Once the ROI is converted to one of these three forms, compare it to the parking spot when it is unoccupied
-Finally, draw onscreen the status of each spot

Steps I have taken:

- Worked on a filter image function that will let me extract the white/yellow lines in a parking lot

Steps I will take:

- Obtain footage of a parkinglot (start simple)



