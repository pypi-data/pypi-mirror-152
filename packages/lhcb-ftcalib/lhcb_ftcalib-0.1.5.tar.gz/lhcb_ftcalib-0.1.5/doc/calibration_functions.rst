Calibration functions
=============================

The raw mistag predictions are calibrated to better model the actual 
mistag probability :math:`\eta\mapsto\omega(\eta)`. The available
calibration functions are listed here.

GLM Polynomials
---------------

.. autoclass:: calibration_functions.PolynomialCalibration
   :members:
   :undoc-members:
   :show-inheritance:

Cubic Spline GLM
----------------

.. autoclass:: calibration_functions.NSplineCalibration
   :members:
   :undoc-members:
   :show-inheritance:


Cubic Spline Model
------------------

.. autoclass:: calibration_functions.BSplineCalibration
   :members:
   :undoc-members:
   :show-inheritance:
