# Pakistan Live Power 🇵🇰

A simple live voting web app built with **Streamlit**. Users pick a party, cast a vote, and instantly see the results as a chart with percentages. An admin panel lets the owner view and reset the data.

**Live app:** https://pak-power.streamlit.app

> This is a learning project and a fun poll. It is not an official or scientific survey.

## Features

- Vote for a party: PTI, PMLN, PPP, JUI-F, MQM, JI, TLP
- One vote per browser session
- Live results with a bar chart, vote counts and percentages
- Password-protected admin panel to view and reset all votes
- Votes stored in a local SQLite database

## Tech Stack

- Python
- Streamlit
- SQLite
- pandas

## Run Locally

1. Clone the repository:
   ```
   git clone https://github.com/zyanhub/Pak-power.git
   cd Pak-power
   ```
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Set the admin password:
   - Windows (PowerShell): `$env:ADMIN_PASSWORD="your-password"`
   - Mac / Linux: `export ADMIN_PASSWORD="your-password"`
4. Start the app:
   ```
   streamlit run app.py
   ```

## Admin Password

The password is never stored in the code. It is read from the `ADMIN_PASSWORD` setting.

- **Streamlit Cloud:** App settings → Secrets, then add `ADMIN_PASSWORD = "your-password"`
- **Locally:** set the `ADMIN_PASSWORD` environment variable as shown above

If no password is set, the admin panel stays locked.

## Project Structure

```
Pak-power/
├── app.py            # Main app (user panel and admin panel)
├── admin.py          # Standalone admin page
├── requirements.txt  # Python dependencies
└── utils/
    ├── auth.py       # Admin password check
    └── db.py         # SQLite database functions
```

## Adding a Party

Open `app.py`, find the `st.selectbox("Select Party", [...])` line and add the new name to the list.

## Known Limitations

- The one-vote limit works per session, so refreshing the page lets a person vote again.
- On Streamlit Cloud the local database can reset when the app restarts, so votes are not permanent. Moving to an online database is planned.

## Author

Made by [zyanhub](https://github.com/zyanhub)
