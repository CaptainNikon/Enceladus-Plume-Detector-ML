PDS_VERSION_ID                  = PDS3                                        
                                                                              
RECORD_TYPE                     = FIXED_LENGTH                                
RECORD_BYTES                    = 80                                          
SPACECRAFT_NAME                 = "CASSINI ORBITER"                           
TARGET_NAME                     = "DUST"                                      
OBJECT                          = TEXT                                        
   PUBLICATION_DATE             = 2006-179                                    
   NOTE                         = "This is the aareadme.txt                   
                                   introductory file for the                  
                                   Cassini Cosmic Dust Analyzer               
                                   data submission #1."                       
END_OBJECT                      = TEXT                                        
END                                                                           
                                                                              
                                                                              
                           VOLUME COCDA_0013                                  
                           Cassini Orbiter                                    
                         Cosmic Dust Analyzer                                 
                                                                              
                     CDA Standard Products Archive                            
                             Entire Mission                                   
                             Small Body Node                                  
                                of the                                        
                         Planetary Data System                                
                                                                              
Introduction                                                                  
===================                                                           
                                                                              
This volume contains the Cassini Orbiter COSMIC DUST ANALYSER (CDA) data      
products from the entire mission, submitted to the Planetary Data System      
(PDS). As of the delivery date, the data set contains data from the           
Interplanetary Cruise phase,covering the time range 2005-203T00:00:01         
and 2005-233T23:59:59. New data will be added on subsequent volumes as        
they become available. This volume also contains documentation                
describing the CDA instrument. Supporting documents and label files for       
the CDA data products conform to the Planetary Data System (PDS)              
Standards Version 3.6. Every effort has been made to ensure that the          
data and documentation are of the best possible quality.  However, all        
users are encouraged to verify the "correctness" of the data prior to         
submitting any publications or other work based on these data. Users of       
these data are encouraged to acknowledge both the PDS and the principal       
investigators of the instruments whose data are used in analysis in all       
publications.                                                                 
                                                                              
The archive producers would like to thank C. Neese and M. Sykes from the      
Small Bodies Node of the Planetary Data System for their help during the      
archiving process.                                                            
                                                                              
Disk Format                                                                   
===================                                                           
                                                                              
The disk has been formatted so that a variety of computer systems (e.g.       
IBM PC, MACINTOSH, SUN) may access the data. Specifically, it is              
formatted according to the UDF_ISO9660_BRIDGE (Universal Disk Format)         
standard.                                                                     
                                                                              
File Formats                                                                  
===================                                                           
                                                                              
All document files and detached label files contain 80-byte fixed-length      
records, with a carriage return character (ASCII 13) in the 79th byte         
and a line feed character (ASCII 10) in the 80th byte. This allows the        
files to be read by the MacOS, DOS, Unix, and VMS operating systems. All      
tabular files are also described by PDS labels, either embedded at the        
beginning of the file or detached. If detached, the PDS label file has        
the same name as the data file it describes, with the extension .LBL;         
for example, the file CDAEVENTS.TAB is accompanied by the detached label      
file CDAEVENTS.LBL in the same directory.                                     
                                                                              
CD-ROM content                                                                
===================                                                           
                                                                              
The files on this CD-ROM are organized in one top-level directory with        
several subdirectories. The following table shows the structure and           
content of these directories. In the table, directory names are enclosed      
in square brackets ([]), upper-case letters indicate an actual directory      
or file name, and lower-case letters indicate the general form of a set       
of directory or file names.                                                   
                                                                              
FILE                   CONTENTS                                               
Top-level directory                                                           
|                                                                             
|- AAREADME.TXT        The File you are reading                               
|                                                                             
|- ERRATA.TXT          Description of known anomalies and errors              
|                      present on this volume.                                
|                                                                             
|- VOLDESC.CAT         A description of the contents of this volume           
|                                                                             
[CATALOG]              A directory containing the catalog                     
|  |                   files with information about the                       
|  |                   CDA dataset, instrument, and mission.                  
|  |                                                                          
|  |-MISSION.CAT         Mission catalog file                                 
|  |-INSTHOST.CAT        Instrument host (spacecraft) catalog file            
|  |-CDAINST.CAT         CDA instrument catalog file                          
|  |-CDADS.CAT           CDA data set catalog file                            
|  |-CDAREFS.CAT         Reference list catalog file                          
|  |-PROJREF.CAT         Project reference list catalog file                  
|  |-DUST.CAT            Target catalog file                                  
|  |-CATINFO.TXT         Description of files in the CATALOG directory        
|                                                                             
[INDEX]                  A directory containing index files for this volume   
|  |                                                                          
|  |-INDEX.TAB           Index of the contents of this volume                 
|  |-INDEX.LBL           Detached label for index                             
|  |-CUMINDEX.TAB        Index of all volumes published to date               
|  |-CUMINDEX.LBL        Detached label for cumulative index                  
|  |-INDXINFO.TXT        Description of files in the INDEX directory          
|                                                                             
|[DATA]                 Directory containing the data products                
|  |                                                                          
|  |-DATAINFO.TXT        Description of files in the DATA directory           
|                                                                             
|  |-CDAAREA.LBL      PDS label object. Description of                        
|  |                  CDA sensitive area data.                                
|  |                                                                          
|  |-CDAAREA.TAB      PDS table object. Sensitive area data.                  
|  |                                                                          
|  |-CDACOUNTER.LBL   PDS label object. Description of                        
|  |                  CDA counter state data.                                 
|  |-CDACOUNTER.TAB   PDS table object. Counter state data.                   
|  |                                                                          
|  |-CDAEVENT.LBL     PDS label object. Description of                        
|  |                  CDA event data.                                         
|  |-CDAEVENT.TAB     PDS table object. Event evaluation data.                
|  |                                                                          
|  |-CDAPOINTING.LBL  PDS label object. Description of                        
|  |                  CDA pointing data.                                      
|  |-CDAPOINTING.TAB  PDS table object. Pointing data.                        
|  |                                                                          
|  |-CDASETTINGS.LBL  PDS label object. Description of                        
|  |                  CDA settings data.                                      
|  |-CDASETTINGS.TAB  PDS table object. Settings data.                        
|  |                                                                          
|  |-CDASPECTRA.LBL   PDS label object. Description of                        
|  |                  CDA TOF mass spectra data.                              
|  |-CDASPECTRA.TAB   PDS table object. TOF mass spectra data.                
|  |                                                                          
|  |-CDASTAT.LBL      PDS label object. Description of                        
|  |                  CDA status data.                                        
|  |-CDASTAT.TAB      PDS table object. CDA status data.                      
|  |                                                                          
|  |-[QISIGNALS]         Directory containing individual                      
|  |  |                  impact signals                                       
|  |  |                  XXXXXXXX represents the id of each signal.           
|  |  |-QI_XXXXXXXX.LBL  PDS label object. Description                        
|  |  |                       of QI signal data.                              
|  |  |-QI_XXXXXXXX.TAB  PDS table object. QI signal data.                    
|  |  |                                                                       
|  |-[QTSIGNALS]         Directory containing individual                      
|  |  |                  impact signals                                       
|  |  |-QT_XXXXXXXX.LBL  PDS label object. Description                        
|  |  |                        of QT signal data.                             
|  |  |-QT_XXXXXXXX.TAB  PDS table object. QT signal data.                    
|  |  |                                                                       
|  |-[QCSIGNALS]         Directory containing individual                      
|  |  |                   impact signals                                      
|  |  |-QC_XXXXXXXX.LBL  PDS label object. Description                        
|  |  |                  of QC signal data.                                   
|  |  |-QC_XXXXXXXX.TAB  PDS table object. QC signal data.                    
|  |  |                                                                       
|  |-[QPSIGNALS]         Directory containing individual                      
|  |  |                  impact signals                                       
|  |  |-QP_XXXXXXXX.LBL  PDS label object. Description                        
|  |  |                  of QP signal data.                                   
|  |  |-QP_XXXXXXXX.TAB  PDS table object. QP signal data.                    
|  |  |                                                                       
|  |-[MPSIGNALS]         Directory containing individual                      
|  |  |                  impact signals                                       
|  |  |-MP_XXXXXXXX.LBL  PDS label object. Description                        
|  |                     of MP signal data.                                   
|  |  |-MP_XXXXXXXX.TAB  PDS table object. MP signal data.                    
|                                                                             
|                                                                             
|-[DOCUMENT]           Directory containing supporting documents              
|                                                                             
   |-Software Interface Specification (SIS)                                   
   |-DOCINFO.TXT     Description of files in the DOCUMENT directory           
                                                                              
This volume contains one data set with the following                          
DATA_SET_ID: CO-D-CDA-3/4/5-DUST-V1.0                                         
                                                                              
Contact Information                                                           
===================                                                           
                                                                              
The medium and supporting files required for delivery were prepared by:       
                                                                              
Nicolas Altobelli, NASA/Jet Propulsion Lab                                    
4800 Oak Grove Drive, Pasadena CA 91101                                       
Mail: nicolas.altobelli@jpl.nasa.gov                                          
Tel: (+1) 818 393 0837                                                        
                                                                              
Sascha Kempf, Max-Planck-Institut                                             
fuer Kernphysik, Postfach 103980                                              
Heidelberg 69029, Germany                                                     
Mail: Sascha.kempf@mpi-hd.mpg.de                                              
Tel: (+49) 6221 516 247                                                       
                                                                              
Contact persons at PDS-SBN:                                                   
                                                                              
Mark V. Sykes, Planetary Science                                              
Institute, 1700 East Ft. Lowell,                                              
Suite 106, Tucson, AZ 85719-2395                                              
Mail: sykes@psi.edu                                                           
Tel: (+1) 520 622 6300                                                        
                                                                              
Carol Neese, Planetary Science                                                
Institute, 1700 East Ft. Lowell,                                              
Suite 106, Tucson, AZ 85719-2395                                              
Mail: neese@psi.edu                                                           
                                                                              
For further information about the individual data products, please            
consult the PDS labels and catalog files specific to the dataset.             
