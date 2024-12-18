## 10xTranslator
The best translator currently available

git repo: https://github.com/tpaau-17DB/10xTranslator


## Dependencies
Make sure you have `git`, `python3` and `pip` installed.

If you don't have `deep_translator` installed, run:

```
pip install deep_translator
```

The program requires a custom logger package that can be downloaded from: https://github.com/tpaau-17DB/python-logger.


## Installing
<details>

<summary>Autoinstall script</summary>


For quick install you can run:

```
./install.sh
```

This script ensures you have all the dependencies required and installs the package. 
Make sure this command is executed from the root of the repository, where `setup.py` is located.

</details>


<details>

<summary>Manual installation</summary>

To manually install the python package you can run `pip install .`
This command needs to be executed from the root of the repository, where `setup.py` is located.

You can also copy the files to `/usr/bin` so translator can be accessed at all times:

```
sudo cp best_translator/translator.py best_translator/utils.py /usr/bin/translator
```

Then ensure `/usr/bin/translator` has required permissions:

```
sudo chmod 755 /usr/bin/translator
```


</details>
