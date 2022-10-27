A = imread("C:\Users\hariv\OneDrive\Desktop\Things\fall-semester\CSE4003 - Cyber Security\project\review-2\Double-Encryption\images\coverImageSecret.png");
ref = imread("C:\Users\hariv\OneDrive\Desktop\Things\fall-semester\CSE4003 - Cyber Security\project\review-2\Double-Encryption\images\coverImage.png");
[peaksnr,snr] = psnr(A, ref); 

disp(peaksnr);
