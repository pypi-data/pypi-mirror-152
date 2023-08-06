Domain adaptation based on optimal transport
--------------------------------------------
Python package to simplify OT-based domain adaptation. This package uses [POT](https://pythonot.github.io/auto_examples/domain-adaptation/plot_otda_color_images.html) as optimal transport backend.

Install with pip
----------------

```bash
$ python3 -m pip install otda --user
```

Install from source
-------------------

```bash
$ python3 setup.py install --user
```

Exemplary code snippet
----------------------

```python                                                                                                      
adapted_im = otda.colour_transfer(source_im, target_im, method='linear', nsamples=1000)
```

Run domain adaptation on a single image
---------------------------------------

```bash
$ python3 -m otda.run --source source.jpg --target target.jpg --output output.jpg --method emd
```
Available methods: linear, gaussian, sinkhorn, emd.


Some examples of the colour adaptation
--------------------------------------

<table>
    <thead>
        <tr>
            <th>Source image</th>
            <th>Target domain image</th>
            <th>Method</th>
            <th>Output</th>
            <th>Computation time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=5><img src="https://github.com/luiscarlosgph/ot-domain-adaptation/blob/main/images/source1.jpg?raw=true" width=640></td>
            <td rowspan=5><img src="https://github.com/luiscarlosgph/ot-domain-adaptation/blob/main/images/target1.jpg?raw=true" width=640></td>
        </tr>
        <tr>
            <td>Linear</td>
            <td><img src="https://github.com/luiscarlosgph/ot-domain-adaptation/blob/main/images/output1_linear.jpg?raw=true" width=640></td>
            <td>0.086s</td>
        </tr>
        <tr>
            <td>Gaussian (n=1000)</td>
            <td><img src="https://github.com/luiscarlosgph/ot-domain-adaptation/blob/main/images/output1_gaussian.jpg?raw=true" width=640></td>
            <td>19.194s</td>
        </tr>
        <tr>
            <td>Sinkhorn (n=1000)</td>
            <td><img src="https://github.com/luiscarlosgph/ot-domain-adaptation/blob/main/images/output1_sinkhorn.jpg?raw=true" width=640></td>
            <td>30.736s</td>
        </tr>
        <tr>
            <td>Earth mover's distance (n=1000)</td>
            <td><img src="https://github.com/luiscarlosgph/ot-domain-adaptation/blob/main/images/output1_emd.jpg?raw=true" width=640></td>
            <td>22.988s</td>
        </tr>
    </tbody>
</table>


License
-------

This repository is shared under an [MIT license](https://github.com/luiscarlosgph/ot-domain-adaptation/blob/main/LICENSE).


Author
------

Luis Carlos Garcia Peraza Herrera (luiscarlos.gph@gmail.com), 2020-2022.
