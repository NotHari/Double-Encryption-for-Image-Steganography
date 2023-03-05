A = imread("C:\projects\Double-Encryption-for-Image-Steganography\images\tulips.png");
ref1 = imread("C:\projects\Double-Encryption-for-Image-Steganography\images\tulipsSecret1.png");
ref2 = imread("C:\projects\Double-Encryption-for-Image-Steganography\images\tulipsSecret2.png");
ref3 = imread("C:\projects\Double-Encryption-for-Image-Steganography\images\tulipsSecret3.png");
ref4 = imread("C:\projects\Double-Encryption-for-Image-Steganography\images\tulipsSecret4.png");
ref5 = imread("C:\projects\Double-Encryption-for-Image-Steganography\images\tulipsSecret5.png");

[peaksnr1,snr1] = psnr(A, ref1); 
[peaksnr2,snr2] = psnr(A, ref2); 
[peaksnr3,snr3] = psnr(A, ref3); 
[peaksnr4,snr4] = psnr(A, ref4); 
[peaksnr5,snr5] = psnr(A, ref5);

disp("PSNR: "+peaksnr1+" "+peaksnr2+" "+peaksnr3+" "+peaksnr4+" "+peaksnr5);
disp("SSIM: "+ssim(A, ref1)+" "+ssim(A, ref2)+" "+ssim(A, ref3)+" "+ssim(A, ref4)+" "+ssim(A, ref5));
disp("MSE: "+immse(A, ref1)+" "+immse(A, ref2)+" "+immse(A, ref3)+" "+immse(A, ref4)+" "+immse(A, ref5));
