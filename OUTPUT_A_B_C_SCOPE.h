!=======A-SCOPE===============================
I=1
!    I=DIS

!!    DO J = 1, ROWS
!!       WRITE(20,*) B_SCAN_IMAGE3(I,1,J)
!        WRITE(20,*) B_SCAN_IMAGE3(J,I,1)
!!    END DO

      DO J = 1, ROWS
         WRITE(20,*) J,I, B_SCAN_IMAGE3(J,I,1) 
      END DO
   
!    WRITE(20,*) (B_SCAN_IMAGE3(I,1,J), J=1,ROWS)
!   PRINT *, (B_SCAN_IMAGE3(I,1,J), J=1,ROWS)
   
!============================================= 
     
!======B_SCAN=================================
!B_SCAN_IMAGE3(ROWS,DIS,TRA)     
!G = TRA
!     DO J = 1, ROWS
!        WRITE(21,*)(B_SCAN_IMAGE3(I,G,J), I=1,DIS)
!     END DO

!=============================================
!    PRINT *, "CHECK",G


!=====C_SCAN_IMAGE============================
!!PRINT *, "PLEASE ENTER THE SAMPLE AMONG 512 ROWS [DEPTH]."
!!READ *, J 

       !DO K=1,TRA 
        !     WRITE(22,*) (B_SCAN_IMAGE3(I,K,J),I=1,DIS)          
       
!        DO I=1,DIS    

!           WRITE(22,*) (B_SCAN_IMAGE3(I,K,J),K=1,TRA)         
!
!        END DO
!    PRINT *, "COMPLETE C_SCAN_IMAGE OUPUT"
!=============================================


!=====3D_CUBE_IMAGE============================
!J=ROWS 
!!     DO J = 1, ROWS

        !FOR PYTHON
        !DO  K = 1, TRA              
        !        WRITE(23,*) (B_SCAN_IMAGE3(I,K,J), I = 1, DIS)         
        !END DO


!!        DO  I = 1, DIS              
!!                WRITE(23,*) (B_SCAN_IMAGE3(I,K,J), K = 1, TRA)         
!!        END DO

!!     END DO
!     PRINT *, "COMPLETE 3D_CUBE_IMAGE OUPUT"
!=============================================

PRINT *, char(7)


