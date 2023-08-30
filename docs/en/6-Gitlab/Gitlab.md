## **IMPORTANT NOTES**

1. Please do NOT store your token _anywhere_ in your workspace server file
   system. Contributors to a namespace will have access to them.
2. If there is a contributor external to Statistics Canada in your namespace,
   you will lose access to cloud main GitLab access!

---

Thankfully, using the cloud main GitLab on the AAW is just like how you would
regularly use git.

### Step 1: Locate the Git repo you want to clone and copy the clone with HTTPS option

If your repository is private, you will need to also do Step 4 (Creating a
Personal Access Token) for this to go through. For me this was a test repo
![image](https://user-images.githubusercontent.com/23174198/217060353-ba229ced-b5c1-4eae-8878-9608835cc65f.png)

### Step 2: Paste the copied link into one of your workspace servers

![image](https://user-images.githubusercontent.com/23174198/217060697-535df6c1-d9bb-4bc3-a42b-9f085a5386d5.png)

### Step 3: Success!

As seen in the above screenshot I have cloned the repo!

### Step 4: Create a Personal Access Token for pushing (also used if pulling from a private repository)

If you try to `git push ....` you will encounter an error eventually leading you
to the
[GitLab help documentation](https://gitlab.k8s.cloud.statcan.ca/help/user/profile/account/two_factor_authentication.md#error-http-basic-access-denied-the-provided-password-or-token-)

You will need to make a Personal Access Token for this. To achieve this go in
GitLab, click your profile icon and then hit `Preferences` and then
`Access Tokens`
![image](https://user-images.githubusercontent.com/23174198/217061060-122dded8-dc80-46ce-a907-a85913cf5dd7.png)
Follow the prompts entering the name, the token expiration date and granting the
token permissions (I granted `write_repository`)

### Step 5: Personalize `Git` to be you

Run `git config user.email ....` and `git config user.name ...` to match your
GitLab identity.

### Step 6: Supply the Generated Token when asked for your password

The token will by copy-able at the top once you hit
`Create personal access token` at the bottom
![image](https://user-images.githubusercontent.com/23174198/217062846-03a715f1-ded5-4d80-ad4b-c647ae5e30fd.png)

Once you have prepared everything it's time
![image](https://user-images.githubusercontent.com/23174198/217063198-c1bd6c3a-ebc5-444d-98ba-24ef32faa20e.png)

### Step 7: See the results of your hard work in GitLab

![image](https://user-images.githubusercontent.com/23174198/217063990-efaa8e81-a0eb-4b6d-842e-2ca3112bb4f7.png)
