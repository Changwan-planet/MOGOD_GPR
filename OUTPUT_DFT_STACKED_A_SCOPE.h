DO I = 1, ROWS

psd(I,1) = 10 * log10(dft_real(I,1)**2 + dft_imag(I,1)**2)

END DO


!======DTF_STACKED_A_SCOPE=============================================
DO I = 1, ROWS
        WRITE(27,*) dft_real(I,1), dft_imag(I,1), psd(I,1), idft_real(I,1), idft_imag(I,1)
END DO
!======================================================================
