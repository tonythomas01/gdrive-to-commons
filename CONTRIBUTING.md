# Contributing 
We welcome features and issue reports. Since the project is associated with the Wikimedia movement, we are moving our 
issue trackers to [Wikimedia Phabricator](https://phabricator.wikimedia.org/project/view/4068). However, feel free to create
an issue here as well. 

Code review and merge happens here on Github as of now. 

## Specific steps to contribute
1. Get a local fork of this repository in your username-space following instructions [here](https://help.github.com/en/articles/about-forks). 
2. Setup your local development environment following the instructions [here](https://github.com/tonythomas01/gdrive_to_commons#steps-for-local-development).
3. We use a `pull-request` model for development. To start contirbuting, you can create a **PR** to the `master` branch following 
the documentation [here](https://help.github.com/en/articles/creating-a-pull-request).
4. Make sure you run all `pre-commit` hooks (will run automatically on `git commit` if you followed instructions on 2 correctly). 
a sample output while committing would be: 
```
(gdrive-env-3.5.3) ➜  gdrive_to_commons git:(master) ✗ git add uploader/templates/
(gdrive-env-3.5.3) ➜  gdrive_to_commons git:(master) ✗ git commit -m "Fix tempalte reidrect, finish up with new template designs"
black....................................................................Passed
prettier.................................................................Failed
hookid: prettier

Files were modified by this hook. Additional output:

uploader/templates/home.html 194ms

(gdrive-env-3.5.3) ➜  gdrive_to_commons git:(master) ✗ git add uploader/templates/     
```
The `pre-commits` automatically fixes the file for you, so feel free to ignore these messages. In case you see that `prettier` 
is messing up with your code, add one of those ignore flags above the line you want to remain intact. 
```
 <label class="custom-control-label" for="customControlInline">
                    <!-- prettier-ignore -->
                    <span> This formatting here will be preserved </span>
</label>
```
5. Any code merged to `master` branch is automatically deployed at our current deployment server. Currently at https://tools.wmflabs.org/google-drive-photos-to-commons/
