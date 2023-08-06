Toy Data Generator
==================

The toy data generator class generates the flavour ground truth of 
a simulated measurement, i.e. the production and detection flavour
as well as a pair of two distributions for the raw and calibrated mistag given
a calibration function with custom parameters. Those parameters can be 
reproduced by calibrating the raw mistag distribution.

The following data are generated:

* **FLAV_PROD**: The true production flavour
* **FLAV_DECAY**: The true decay flavour
* **FLAV_PRED**: The predicted production flavour given the decay flavour and the decay time
* **TOYX_DEC**: The tagging decisions of toy tagger Nr. X
* **TOYX_ETA**: The raw mistag distribution of toy tagger Nr. X
* **TOYX_OMEGA**: The calibrated mistag distribution of toy tagger Nr. X
* **TAU**: If osc=True: The generated decay time distribution
* **OSC**: If osc=True: 1 if B meson of entry has oscillated, else 0
* **eventNumber**: An event counter


.. autoclass:: toy_tagger.ToyDataGenerator
   :members:
   :special-members: __call__


Example use
-----------

.. code-block:: python

   import lhcb_ftcalib as ft

   gen = ft.toy_tagger.ToyDataGenerator()
   df = gen(
    N            = 50000,
    func         = ft.calibration_functions.PolynomialCalibration(2, ft.link.logit),
    params       = [[0, 1, 0, 1], [0.1, 0.9, -0.1, 1.1]],
    osc          = True,
    tagger_types = ["OSKaon", "SSPion"],
    lifetime     = 1.52,  # ps
    DM           = 0.5065,  # ps^-1
    DG           = 0,
    Aprod        = 0.01,
    tag_effs     = [0.4, 0.8]
   )
