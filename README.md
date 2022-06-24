# Blockchain_implementation-Certificate_Management_System

## Description
Managing student’s information and sharing them or giving access to unauthorized people in a much secured way is one of the major responsibilities of any academic institution or course provider. Instead of storing the certificates in a normal database, blockchain technology can be used to store the certificates. In this solution, the certificates will be uploaded to the blockchain and will be shared securely when any third party that needs to access and verify the certificates. 

This is done to curb the prevalence of fake academic certificates that are sometimes not detected during the vetting process for different jobs and especially when recruiting candidates in organizations.

Blockchain is a trusted distributed ledger with shared business processes. It has the following desirable features which aid in the resolution of the problem at hand: 
  It is distributed.
  Permissioned.
  Allows for provenance and immutability.
  
## Overview and purpose of the system / product
The objective of the system is to digitize the academic certificates of students/course participants who obtain academic qualifications any institution, in an immutable, non-repudiable and easily verifiable way to contribute to greater transparency and improve efficiency in the verification of academic certificates.

## System content (system boundaries)
These boundaries determine the scope of responsibility for all aspects of the system.

1. **Issuing**: In this step the claim, issuer, evidence, recipient and signature are recorded onto a certificate. Additionally, this information can be stored in a centralized database of claims.
2. **Verification**: A third party verifies the authenticity of the certificate. This includes verification of security features built into the certificate such as a digital signature with the original issuer or verification against a centralized database of claims hosted by a third party.
3. **Sharing**: The certificate recipient shares the certificate with a third party.

## Interaction (potential) of the product (with other products and components)
Third party stake holders such as employers, recruitment organizations or academic institutions may leverage on the solution to store academic certificates on the blockchain and use the technology to verify said certificates.

## Product features (short description)
An effective certification system is one in which certificates are widely accepted as proof of claims. This implies that the recipients of the certificates trust the system. This trust is created in the following ways: 

**Identity Verification**: This involves verifying the identity of both the issuer and the certificate holder. This is done either through identity documents, which are certificates themselves, or third parties.

**Standard Issue and Certification Processes**: This involves having an open, predictable and equitable method of issuing certificates. This especially applies in a scenario where a system has multiple issuers.

**Accessibility**.

**Security**.

## Security requirements

**Transparency and provenance**. Gives individuals the ability to access data on the origins of each certificate and its ownership. The system can indisputably prove that a particular certificate was issued at a particular point in time.

**Self-sovereignty and Identity**.

**Disintermediation**: This refers to replacing middlemen in transactions. Participants in the system can quickly prove ownership or authorship of certificates without the need of a central authority.

**Immutability**: This refers to the fact that records on the Blockchain cannot be altered after they are created.


## Characteristics of users (who is the end user of the system)
Employers looking to verify applicants' certificates.

Recruitment organisations looking to verify applicants' certificates.

Academic institutions (Faculty Admins) looking to issue certificates.

Course porividers/Organizations looking to issue certificates.

## Restrictions

Performance: The need to cope with processing a large flow of transactions with the need to synchronize validators which takes time.
