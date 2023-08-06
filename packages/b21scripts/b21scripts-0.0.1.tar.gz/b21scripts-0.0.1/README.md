# b21scripts

Various scripts, libraries and modules to help with manipulating data and files associated with SAXS experiments and data analysis and particularly suited to the workflow at the B21 SAXS beamline, Diamond Light Source.

## readwrite
    
The readwrite libraries provied a convenient way to parse various files that might be associated with a SAXS experiment such as .dat files, .pdb files describing molecular structures that may have been downloaded from the [Protein Data Bank](https://www.rcsb.org/), fit files giving the fit of a model to experimental data and out files containing the output from the indirect Fourier transform as produced by the [ATSAS](https://www.embl-hamburg.de/biosaxs/software.html) program [Gnom](https://www.embl-hamburg.de/biosaxs/gnom.html).

---

### Modules

1. readwrite.dat.DAT
Functions for reading and writing files of type .dat containing three columns of SAXS data, scattering vector Q, intensity and error.
