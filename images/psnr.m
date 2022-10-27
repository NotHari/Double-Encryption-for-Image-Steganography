A = imread("C:\Users\hariv\OneDrive\Desktop\THINGS\fall-semester\CSE4003 - Cyber Security\project\review-2\Double-Encryption\images\coverImage.png");
ref = imread("C:\Users\hariv\OneDrive\Desktop\THINGS\fall-semester\CSE4003 - Cyber Security\project\review-2\Double-Encryption\images\coverImageSecret.png");
[peaksnr,snr] = psnr(A, ref); 

disp(peaksnr);
