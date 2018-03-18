# Example Post Mortem

## Summary Information

- **Incident ID:** 1234
- **Date:** 15-01-2018
- **Authors:** Davy, Jeff, Someone
- **Status:** In-Progress|Complete
- **Summary:** Something happened, it got fixed.
- **Impact:** Queries stopped working
- **Root Causes:** Issue with the thing
- **Trigger:** Bug
- **Resolution:** Fixed it
- **Detection:** Monitoring Alert

## Action Items

|Action Item                                                          |Type    |Owner|Ticket ID |
|---------------------------------------------------------------------|--------|-----|----------|
|Update playbook with instructions for responding to cascading failure|mitigate|Davy |n/a TODO  |
|Use flux capacitor to balance load between clusters                  |prevent |Jeff |issue-1234|
|Schedule cascading failure test during next DiRT                     |process |Sarah|n/a TODO  |

## Lessons Learned

### What Went Well

- Monitoring picked up issue quickly
- Rapidly distributed updated Shakespeare corpus to all clusters

#### What Went Wrong

- We’re out of practice in responding to cascading failure
- We exceeded our availability error budget (by several orders of magnitude) due to the exceptional surge of traffic that essentially all resulted in failures

#### Where we got lucky

- Mailing list of Shakespeare aficionados had a copy of new sonnet available
- Server logs had stack traces pointing to file descriptor exhaustion as cause for crash
- Query-of-death was resolved by pushing new index containing popular search term

## Timeline

### 03-04-2017 (All Times UTC)

- *14:51* News reports that a new Shakespearean sonnet has been discovered in a Delorean’s glove compartment
- *14:53* Traffic to Shakespeare search increases by 88x after post to /r/shakespeare points to Shakespeare search engine as place to find new sonnet (except we don’t have the sonnet yet)
- *14:54* OUTAGE BEGINS — Search backends start melting down under load
- *14:55* docbrown receives pager storm, ManyHttp500s from all clusters
- *14:57* All traffic to Shakespeare search is failing: see http://monitor
- *14:58* docbrown starts investigating, finds backend crash rate very high

## Supporting Information

- [Link to Something](http://example.com)