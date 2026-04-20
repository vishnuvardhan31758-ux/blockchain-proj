from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import json
from web3 import Web3, HTTPProvider

global username
global contract, web3
global usersList, evidenceList

contract = None
web3 = None
usersList = []
evidenceList = []


# ---------------- BLOCKCHAIN CONNECTION ----------------
def getContract():
    global contract, web3
    try:
        blockchain_address = 'http://127.0.0.1:9545'
        web3 = Web3(HTTPProvider(blockchain_address))

        if web3.is_connected():
            web3.eth.default_account = web3.eth.accounts[0]

            with open('Evidence.json') as file:
                contract_json = json.load(file)
                contract_abi = contract_json['abi']

            contract = web3.eth.contract(
                address='0xA3413AeAf290AfD3f317B8CA02b2B45AFDB046CE',
                abi=contract_abi
            )
        else:
            contract = None
    except:
        contract = None


# ---------------- FETCH DATA ----------------
def getUsersList():
    global usersList, contract
    usersList = []
    if contract is None:
        return
    count = contract.functions.getUserCount().call()
    for i in range(count):
        usersList.append([
            contract.functions.getUsername(i).call(),
            contract.functions.getPassword(i).call(),
            contract.functions.getPhone(i).call(),
            contract.functions.getEmail(i).call(),
            contract.functions.getStationaddress(i).call(),
            contract.functions.getOfficerType(i).call()
        ])


def getEvidenceList():
    global evidenceList, contract
    evidenceList = []
    if contract is None:
        return
    count = contract.functions.getEvidenceCount().call()
    for i in range(count):
        evidenceList.append([
            contract.functions.getEvidenceid(i).call(),
            contract.functions.getOfficername(i).call(),
            contract.functions.getReportedcrime(i).call(),
            contract.functions.getCrimedetails(i).call(),
            contract.functions.getEvidencedetails(i).call(),
            contract.functions.getCrimearea(i).call(),
            contract.functions.getWitnessname(i).call(),
            contract.functions.getWitnesscontact(i).call(),
            contract.functions.getCrimedate(i).call()
        ])


# ---------------- BASIC PAGES ----------------
def index(request):
    return render(request, 'index.html')


def AdminLogin(request):
    return render(request, 'AdminLogin.html')


def OfficerLogin(request):
    return render(request, 'OfficerLogin.html')


def AddOfficer(request):
    return render(request, 'AddOfficer.html')


def AddEvidences(request):
    return render(request, 'AddEvidences.html')


# ---------------- LOGIN ----------------
def AdminLoginAction(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('t1')
        password = request.POST.get('t2')

        if username == "admin" and password == "admin":
            return HttpResponse("Welcome Admin")
        return HttpResponse("Invalid Login")


def OfficerLoginAction(request):
    getContract()
    if contract is None:
        return HttpResponse("Blockchain not running")

    getUsersList()

    if request.method == 'POST':
        global username
        username = request.POST.get('t1')
        password = request.POST.get('t2')

        for u in usersList:
            if u[0] == username and u[1] == password:
                return HttpResponse("Welcome Officer")

        return HttpResponse("Invalid Login")


# ---------------- ADD OFFICER ----------------
def AddOfficerAction(request):
    getContract()
    if contract is None:
        return HttpResponse("Blockchain not running")

    if request.method == 'POST':
        getUsersList()

        username = request.POST.get('t1')
        password = request.POST.get('t2')
        contact = request.POST.get('t3')
        email = request.POST.get('t4')
        address = request.POST.get('t5')
        officer_type = request.POST.get('t6')

        for u in usersList:
            if u[0] == username:
                return HttpResponse("User already exists")

        msg = contract.functions.createUser(
            username, password, contact, email, address, officer_type
        ).transact()

        web3.eth.wait_for_transaction_receipt(msg)

        return HttpResponse("Officer Added Successfully")


# ---------------- VIEW DATA ----------------
def ViewOfficer(request):
    getContract()
    if contract is None:
        return HttpResponse("Blockchain not running")

    getUsersList()

    output = "<h2>Officer List</h2><table border=1>"
    for u in usersList:
        output += f"<tr><td>{u[0]}</td><td>{u[2]}</td></tr>"
    output += "</table>"

    return HttpResponse(output)


def ViewEvidence(request):
    getContract()
    if contract is None:
        return HttpResponse("Blockchain not running")

    getEvidenceList()

    output = "<h2>Evidence List</h2><table border=1>"
    for e in evidenceList:
        output += f"<tr><td>{e[0]}</td><td>{e[1]}</td></tr>"
    output += "</table>"

    return HttpResponse(output)


# ---------------- ACCESS EVIDENCE ----------------
def AccessEvidence(request):
    getContract()
    if contract is None:
        return HttpResponse("Blockchain not running")

    getEvidenceList()

    output = "<form method='POST' action='/AccessEvidenceAction'>"
    output += "<select name='t1'>"

    for e in evidenceList:
        output += f"<option value='{e[0]}'>{e[0]}</option>"

    output += "</select>"
    output += "<input type='submit' value='View'>"
    output += "</form>"

    return HttpResponse(output)


def AccessEvidenceAction(request):
    getContract()
    if contract is None:
        return HttpResponse("Blockchain not running")

    getEvidenceList()

    if request.method == 'POST':
        eid = request.POST.get('t1')

        for e in evidenceList:
            if e[0] == eid:
                return HttpResponse(f"Evidence Details: {e}")

        return HttpResponse("Not Found")


# ---------------- ADD EVIDENCE ----------------
def AddEvidencesAction(request):
    getContract()
    if contract is None:
        return HttpResponse("Blockchain not running")

    if request.method == 'POST':
        getEvidenceList()

        eid = str(len(evidenceList) + 1)
        crime = request.POST.get('t1')
        crime_details = request.POST.get('t2')
        evidence = request.POST.get('t3')
        area = request.POST.get('t4')
        witness = request.POST.get('t5')
        witness_phone = request.POST.get('t6')
        crime_date = request.POST.get('t7')

        image = request.FILES['t8']
        fs = FileSystemStorage()

        msg = contract.functions.createEvidence(
            eid, username, crime, crime_details,
            evidence, area, witness, witness_phone, crime_date
        ).transact()

        web3.eth.wait_for_transaction_receipt(msg)

        fs.save('EvidenceApp/static/files/' + eid + ".png", image)

        return HttpResponse("Evidence Added Successfully")