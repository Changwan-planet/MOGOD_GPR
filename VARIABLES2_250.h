!==================================
INTEGER, PARAMETER :: ROWS=512     !J 512
INTEGER, PARAMETER :: DIS=2300  !I
INTEGER, PARAMETER :: TRA=50       !G
!==================================


!===========================================================
!MOGOD_GPR require 2-Byte input!
INTEGER*2, DIMENSION(DIS,TRA,ROWS) :: B_SCAN_IMAGE
!REAL*8, DIMENSION(ROWS,DIS,TRA) :: B_SCAN_IMAGE2
REAL*8, DIMENSION(DIS,TRA,ROWS) :: B_SCAN_IMAGE2


!============================================================      

!============================================================
REAL*8, DIMENSION(1:ROWS,1) :: HIBERT_SIGNAL

REAL*8, DIMENSION(1:ROWS,1) :: f_real
REAL*8, DIMENSION(1:ROWS,1) :: f_imag


INTEGER             :: I,J,K,G,P,R, SAMPLE
REAL*8              :: BGR

!=============================================================
!CHARACTER (LEN=11)  :: FH1='201223__0'
!CHARACTER (LEN=11)  :: FH1='210201__0'
!CHARACTER (LEN=11)  :: FH1='201223__0'
CHARACTER (LEN=17)  :: FH1='f1-250-profile-'
CHARACTER (LEN=4)  :: FT='.rd3'
CHARACTER (LEN=22) :: ITEM_NUMBER


!PRINT *, FH1


