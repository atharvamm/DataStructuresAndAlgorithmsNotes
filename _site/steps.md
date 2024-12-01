To create a copy of a GitHub repository in your own account with a different name, you can follow these steps:

1. **Fork the Repository:**
   - Go to the repository you want to copy.
   - Click on the "Fork" button at the top right corner. This will create a fork (copy) of the repository in your GitHub account.

2. **Clone the Forked Repository Locally:**
   - Clone the forked repository to your local machine. Replace `your-username` and `original-repo-name` with your GitHub username and the repository name.
   ```sh
   git clone https://github.com/your-username/original-repo-name.git
   ```

3. **Rename the Local Repository Folder:**
   - Rename the folder to your desired repository name.
   ```sh
   mv original-repo-name new-repo-name
   ```

4. **Change Directory to the New Repository Folder:**
   ```sh
   cd new-repo-name
   ```

5. **Change the Remote URL:**
   - Remove the existing remote URL.
   ```sh
   git remote remove origin
   ```

   - Add a new remote URL pointing to the new repository you will create.
   ```sh
   git remote add origin https://username:token@github.com/your-username/new-repo-name.git
   ```

6. **Create a New Repository on GitHub:**
   - Go to your GitHub account.
   - Click on the "+" icon at the top right corner and select "New repository."
   - Enter the new repository name (`new-repo-name`), and complete the creation process.

7. **Push the Local Repository to the New GitHub Repository:**
   ```sh
   git push -u origin main
   ```

   If your default branch is `master` or another name, use that instead of `main`.



```
MathJax in HTML
Inline Equations: Use \( ... \) for inline equations. These will be the same size as the surrounding text.

Block Equations: Use \[ ... \] for block equations.
```

```
<li><a href="src/tp.html">Tp</a></li> = If you create html file from base
<li><a href="src/first/index.html">First</a></li> = If you use jekyll
```

```
To Build and Check
- bundle exec jekyll build
- bundle exec jekyll serve
```

