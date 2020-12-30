**Compute the Hubble constant and universe average matter density from supernova measurements.**

Mathematical models parametrized by the Hubble constant and matter density are numerically fitted to supernova magnitude and distance data, giving as a result the values of the Hubble constant and matter density that best fit the data.

The various models are named by what reality they presume, and what data they operate on, as listed in this table:
```
+----------------------+--------------------+-------------+
| Models by input      | 5*log(function)+25 | function    |
|                      | [mag_Data]         | [D_L_Data]  |
+----------------------+--------------------+-------------+
| Dark energy          | logDE_mag          | InterDE_D_L |
| integration required |                    |             |
+----------------------+--------------------+-------------+
| Spacetime            | logST_mag          | ST_D_L      |
| no integration       |                    |             |
+----------------------+--------------------+-------------+
| Integrated spacetime | logInterST_mag     | InterST_D_L |
| (optional)           |                    |             |
+----------------------+--------------------+-------------+
```
