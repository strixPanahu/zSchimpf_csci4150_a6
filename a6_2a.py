from numpy import linspace
from matplotlib import pyplot


vertical_shift = linspace(0, 10, 500)

chromatic_values = (vertical_shift
                    * (vertical_shift - 1)
                    * (vertical_shift - 2)
                    * (vertical_shift - 3)
                    * (vertical_shift - 4)
                    * (vertical_shift - 5)
                    * (vertical_shift - 6))

pyplot.figure(figsize=(10, 6))

pyplot.title("Chromatic Polynomial: $k(k-1)(k-2)(k-3)(k-4)(k-5)(k-6)$")
pyplot.xlabel("k (Number of Colors)")
pyplot.ylabel("Chromatic Polynomial Value")

pyplot.plot(vertical_shift, chromatic_values, label=r"$k(k-1)(k-2)(k-3)(k-4)(k-5)(k-6)$")

pyplot.axhline(0, color='black', linewidth=1, linestyle='--')
pyplot.grid(True, linestyle='--', alpha=1)
pyplot.legend()

pyplot.show()
