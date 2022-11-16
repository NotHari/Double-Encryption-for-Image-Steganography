A = imread("C:\Users\hariv\OneDrive\Desktop\Things\fall-semester\CSE4003 - Cyber Security\project\review-2\Double-Encryption\images\coverImage1.png");
ref = imread("C:\Users\hariv\OneDrive\Desktop\Things\fall-semester\CSE4003 - Cyber Security\project\review-2\Double-Encryption\images\coverImageSecret1.png");
[peaksnr,snr] = psnr(A, ref); 

disp(peaksnr);

% A = imread("C:\Users\hariv\OneDrive\Desktop\Things\fall-semester\CSE4003 - Cyber Security\project\review-2\Double-Encryption\images\coverImage2.png");
% ref = imread("C:\Users\hariv\OneDrive\Desktop\Things\fall-semester\CSE4003 - Cyber Security\project\review-2\Double-Encryption\images\coverImageSecret2.png");
% [peaksnr,snr] = psnr(A, ref); 

% disp(peaksnr);

% A = imread("C:\Users\hariv\OneDrive\Desktop\Things\fall-semester\CSE4003 - Cyber Security\project\review-2\Double-Encryption\images\coverImage3.png");
% ref = imread("C:\Users\hariv\OneDrive\Desktop\Things\fall-semester\CSE4003 - Cyber Security\project\review-2\Double-Encryption\images\coverImageSecret3.png");
% [peaksnr,snr] = psnr(A, ref); 

% disp(peaksnr);


