# Host Based Security Monitoring Dashboard
Projects class project idea

My cybersecurity monitoring system will collect system activity, analyze the events, identify suspicious behavior, and display it to a web dashboard. 

I will be using my host pc as the monitored test system, so I can control the environment to ensure it works as intended.

The project will start small and become more advanced throughout the semester as additional monitoring and dashboard features are added.


Initial Goals:
- Monitor file changes on the host computer
- Monitor running processes
- Store events in a database
- Display events on a security dashboard
- Allow the user to review alerts


Planned Technologies
- Python (security monitoring logic)
- SQLite (stores the events and alerts monitor)
- FastAPI (connects python monitor, database, and dashboard)
- React (builds the visual security dashboard to see in browser, shows alerts, events, security levels, etc)
- GitHub (stores my project code, readme, notes, system diagram, and work history)


Probable features: 
- collect security events from host pc
- monitor system activity
- store security events in database
- detect file changes / running processes
- create alerts
- display to dashboard

System Diagram:
- Monitored Computer
        ↓
- Security Monitor
         ↕
- Database
         ↕
- Security Dashboard
        ↕
- User
  




