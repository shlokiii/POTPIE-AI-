# Intelli-Log

Intelli-Log is a real-time logging SDK + CLI monitor for developers and teams who want to:

✅ Track logs across multiple environments  
✅ View real-time logs in terminal  
✅ See alerts on high error rate  
✅ Filter logs by environment/app  
✅ Export logs easily  
✅ All without any frontend!

---

## Features

- Real-time log monitoring with `socket.io`
- API-key-based authentication
- Log levels: `info`, `warn`, `error`, `debug`
- CLI monitoring interface
- Auto-retry on failed sends
- Alert if error rate exceeds threshold
- Export logs to `.txt` via CLI
- Supports multiple environments/apps

---

## Installation

```sh
npm install intelli-log
```
###  Register and Get API Key

You **must register a user and get a project API key** (using Postman or `curl`) to use Intelli-Log.

```http
POST http://localhost:5001/api/auth/register
```
Content-Type: application/json

{
  "email": "your@email.com",
  "password": "yourpassword"
}

response:
```sh
{
  "token": "...",
  "email": "your@email.com",
  "project": {
    "apiKey": "YOUR_GENERATED_API_KEY"
  }
  ```

---


## SDK Usage

###In your Node.js app:

```sh
const IntelliLog = require('intelli-log');

const logger = new IntelliLog({
  apiKey: 'YOUR_API_KEY',
  application: 'MyApp',
  environment: 'production'
});

logger.ready().then(() => {
  logger.info('App started successfully');
  logger.error('Database connection failed');
});
```

### Simulate Logs:
```sh
logger.debug('Debugging variable x...');
logger.warn('This might be an issue...');
logger.error('Something critical broke!');
```
---

### CLI Realtime Log Monitor
## Launch your terminal-based live log monitor with:

```sh
npx intelli-monitor
```

##Live Output:

```sh
📡 IntelliLog Realtime Monitor Started...
✅ Connected to Intelli-Log backend

[12:01:05] [INFO] [MyApp] [production] - Server started
[12:01:08] [ERROR] [MyApp] [production] - DB query failed
```

### Export Logs
While the monitor is running, press e on your keyboard.
Logs will be saved to logs_export.txt in the same directory.


### Auto Alerts on High Error Rate
## If your app emits more than 5 error logs in 15 seconds, IntelliLog will alert you automatically inside the CLI monitor:

```sh
🚨 ALERT: High error rate detected!
More than 5 errors in the last 15 seconds.
```

To simulate:
```sh
for (let i = 0; i < 10; i++) {
  logger.error(`Simulated error ${i}`);
}
```


###  Filter Support (CLI)
Want to only see logs for a specific app or environment?

Update monitor.js to apply custom filters like:

```sh
const APP_FILTER = 'MyApp';
const ENV_FILTER = 'production';

if (log.application !== APP_FILTER || log.environment !== ENV_FILTER) return;
```
(Coming soon: CLI arguments for filtering)


### Installation
## Install the SDK into your app:

```sh
npm install intelli-log
```
Install the monitor CLI:
```sh
npm install -g intelli-monitor
```

