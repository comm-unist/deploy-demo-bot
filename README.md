# deploy-demo-bot

Hello everyone!

As I've promised, the following are the steps to run and deploy your Telegram bots to Heroku.

Enjoy!

_PS. If you have any questions, either PM me on Telegram or just open an issue right here!_

## First Steps - Git

You might want to learn what a `git` is 😌.

_I believe, [this tutorial](https://www.elegantthemes.com/blog/resources/git-and-github-a-beginners-guide-for-complete-newbies)
can make things a lot easier for starters._

The first thing you should do is to create your own repository on GitHub:

1. Login
2. Press the `+` button at the top.
3. To make things easier, opt-in to include a README file when prompted.
4. Follow the steps there.
5. Clone the repository via `$ git clone <your url>` (without `<>`).

## Your First Lines of Code with Github

After you've cloned the repo, move to the folder of your project in Terminal.
Do: `$ cd <project folfer>`.

Then create or copy your code in there. We will create ours from scratch:

1. `$ touch bot.py`
2. `$ vim bot.py` (you might wanna google about using vim 🤪)
3. Edit your code and save it.
4. Add your changes to git: `$ git add bot.py`. (Make sure you've configured your git. If not, [follow these steps](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).)
5. Create your commit message: `$ git commit -m 'Your Message Goes Here 😏'`.
6. Upload (push) your changes to GitHub: `$ git push`. Here git will ask for your credentials - enter them.
