Postmortem: Web Stack Outage

Issue Summary:

Duration:
Start Time: November 15, 2023, 14:30 UTC
End Time: November 16, 2023, 03:45 UTC
Impact:
The outage affected the primary web application, resulting in a 30% drop in user accessibility and performance degradation for the remaining 70%. Users experienced slow page loads, timeouts, and intermittent errors.
Root Cause:
The outage was caused by an unexpected surge in database connections, exhausting the connection pool and leading to a cascading failure in the application's core functionalities.
Timeline:

Detection:

November 15, 2023, 14:30 UTC
Detected through a spike in error rates and latency metrics on the monitoring dashboard.
Actions Taken:

Investigated network connectivity issues first, assuming it might be a networking problem.
Checked server logs for anomalies and errors but found nothing conclusive.
Assumed a DDoS attack, initiated DDoS mitigation measures.
Escalated to the DevOps and Database teams for further investigation.
Misleading Paths:

Initially suspected issues with load balancers due to intermittent user complaints.
Explored the possibility of a code deployment gone wrong, rolling back recent changes but seeing no improvement.
Considered an external attack due to increased traffic but found no evidence in the network logs.
Escalation:

Escalated to the DevOps and Database teams after initial investigations yielded no clear cause.
Involved senior engineers and database administrators to expedite resolution.
Resolution:

Identified the surge in database connections as the root cause.
Temporarily increased the connection pool to bring the application back online.
Implemented a longer-term solution by optimizing database queries and introducing connection throttling to prevent future surges.
Root Cause and Resolution:

Root Cause:

The surge in database connections was triggered by a combination of increased user traffic and inefficient database queries, causing the connection pool to exhaust.
Resolution:

Short-term resolution involved manually increasing the connection pool to stabilize the system.
Long-term resolution included optimizing database queries to reduce the number of open connections and implementing connection throttling to prevent excessive connections from impacting the system.
Corrective and Preventative Measures:

Improvements:

Strengthen monitoring capabilities to detect early signs of connection pool exhaustion.
Enhance communication channels between development, operations, and database teams to expedite issue resolution.
Tasks:

Implement automated scaling for the connection pool to handle traffic spikes.
Conduct a comprehensive review of database queries and optimize for efficiency.
Enhance DDoS detection mechanisms to differentiate between genuine traffic spikes and malicious attacks.
Conduct a post-incident review meeting to share learnings and identify additional preventative measures.
