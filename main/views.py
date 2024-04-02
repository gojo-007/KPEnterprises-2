from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
from main.models import CostCodeModel,ClusterModel,GSTModel,LabourModel,PartyModel,RateModel

def Login(request):
    if request.method=="POST":
        username=request.POST.get('Username')
        password=request.POST.get('Password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,"login.html")

def Logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='Login')
def home(request):
    return render(request,'dashboard.html')

@login_required(login_url='Login')
def Cluster(request):
    data=ClusterModel.objects.all()
    if request.method=="POST":    
        Name=request.POST.get('Name')
        Amount=request.POST.get('Amount')
        if request.POST.get('ATM'):
            ATM='True'
        else:
            ATM='False'
        if request.POST.get('Branch'):
            Branch='True'
        else:
            Branch='False'
        dt=ClusterModel.objects.create(Name=Name,Amount=Amount,ATM=ATM,Branch=Branch)
        dt.save()
        return redirect('/Cluster')
    return render(request,'cluster.html',{'data':data})

@login_required(login_url='Login')
def EditCluster(request,id):
    data=ClusterModel.objects.get(id=id)
    if request.method=="POST":    
        data.Name=request.POST.get('Name')
        data.Amount=request.POST.get('Amount')
        if request.POST.get('ATM'):
            data.ATM='True'
        else:
            data.ATM='False'
        if request.POST.get('Branch'):
            data.Branch='True'
        else:
            data.Branch='False'
        data.save()
        return redirect('/Cluster')
    return render(request,'editcluster.html',{'data':data})

@login_required(login_url='Login')
def DeleteCluster(request,id):
    data=ClusterModel.objects.get(id=id)
    data.delete()
    return redirect('/Cluster')

@login_required(login_url='Login')
def CallEntry(request):
    return render(request,'callentry.html')

@login_required(login_url='Login')
def AddCallEntry(request):
    return render(request,'addcallentry.html')

@login_required(login_url='Login')
def CostCode(request):
    data=CostCodeModel.objects.all()
    if request.method=="POST":    
        CostCode=request.POST.get('CostCode')
        Name=request.POST.get('Name')
        Remarks=request.POST.get('Remarks')
        dt=CostCodeModel.objects.create(CostCode=CostCode,Name=Name,Remarks=Remarks)
        dt.save()
        return redirect('/CostCode')
    return render(request,'costcode.html',{'data':data})

@login_required(login_url='Login')
def EditCostCode(request,id):
    data=CostCodeModel.objects.get(id=id)
    if request.method=="POST":    
        data.CostCode=request.POST.get('CostCode')
        data.Name=request.POST.get('Name')
        data.Remarks=request.POST.get('Remarks')
        data.save()
        return redirect('/CostCode')
    return render(request,'editcostcode.html',{'data':data})

@login_required(login_url='Login')
def DeleteCostCode(request,id):
    data=CostCodeModel.objects.get(id=id)
    data.delete()
    return redirect('/CostCode')

@login_required(login_url='Login')
def GST(request):
    data=GSTModel.objects.all()
    if request.method=="POST":    
        GSTName=request.POST.get('GSTName')
        SGST=request.POST.get('SGST')
        CGST=request.POST.get('CGST')
        dt=GSTModel.objects.create(GSTName=GSTName,SGST=SGST,CGST=CGST)
        dt.save()
        return redirect('/GST')
    return render(request,'GST.html',{'data':data})

@login_required(login_url='Login')
def EditGST(request,id):
    data=GSTModel.objects.get(id=id)
    if request.method=="POST":    
        data.GSTName=request.POST.get('GSTName')
        data.SGST=request.POST.get('SGST')
        data.CGST=request.POST.get('CGST')
        data.save()
        return redirect('/GST')
    return render(request,'editgst.html',{'data':data})

@login_required(login_url='Login')
def DeleteGST(request,id):
    data=GSTModel.objects.get(id=id)
    data.delete()
    return redirect('/GST')

@login_required(login_url='Login')
def Party(request):
    data=PartyModel.objects.all()
    return render(request,'party.html',{'data':data})

@login_required(login_url='Login')
def AddParty(request):
    data=ClusterModel.objects.all()
    if request.method=="POST":    
        Code=request.POST.get('Code')
        PartyName=request.POST.get('PartyName')
        Cluster=request.POST.get('Cluster')
        City=request.POST.get('City')
        Branch=request.POST.get('Branch')
        Address=request.POST.get('Address')
        GSTNo=request.POST.get('GSTNo')
        NO1=request.POST.get('NO1')
        NO2=request.POST.get('NO2')
        NO3=request.POST.get('NO3')
        NO4=request.POST.get('NO4')
        NO5=request.POST.get('NO5')
        NO6=request.POST.get('NO6')
        dt=PartyModel.objects.create(Code=Code,PartyName=PartyName,Cluster=Cluster,City=City,Branch=Branch,Address=Address,GSTNo=GSTNo,NO1=NO1,NO2=NO2,NO3=NO3,NO4=NO4,NO5=NO5,NO6=NO6)
        dt.save()
        return redirect('/Party')
    return render(request,'addparty.html',{'data':data})

@login_required(login_url='Login')
def EditParty(request,id):
    data=PartyModel.objects.get(id=id)
    Clr=ClusterModel.objects.all()
    if request.method=="POST":    
        data.Code=request.POST.get('Code')
        data.PartyName=request.POST.get('PartyName')
        data.Cluster=request.POST.get('Cluster')
        data.City=request.POST.get('City')
        data.Branch=request.POST.get('Branch')
        data.Address=request.POST.get('Address')
        data.GSTNo=request.POST.get('GSTNo')
        data.NO1=request.POST.get('NO1')
        data.NO2=request.POST.get('NO2')
        data.NO3=request.POST.get('NO3')
        data.NO4=request.POST.get('NO4')
        data.NO5=request.POST.get('NO5')
        data.NO6=request.POST.get('NO6')
        data.save()
        return redirect('/Party')
    return render(request,'editparty.html',{'data':data,'Clr':Clr})

@login_required(login_url='Login')
def DeleteParty(request,id):
    data=PartyModel.objects.get(id=id)
    data.delete()
    return redirect('/Party')

@login_required(login_url='Login')
def Labour(request):
    data=LabourModel.objects.all()
    return render(request,'labour.html',{'data':data})

@login_required(login_url='Login')
def AddLabour(request):
    if request.method=="POST":    
        Name=request.POST.get('Name')
        Address=request.POST.get('Address')
        Mobile1=request.POST.get('MobileNo1')
        Mobile2=request.POST.get('MobileNo1')
        Remarks=request.POST.get('Remarks')
        dt=LabourModel.objects.create(Name=Name,Address=Address,Mobile1=Mobile1,Mobile2=Mobile2,Remarks=Remarks)
        dt.save()
        return redirect('/Labour')
    return render(request,'addlabour.html')

@login_required(login_url='Login')
def EditLabour(request,id):
    data=LabourModel.objects.get(id=id)
    if request.method=="POST":    
        data.Name=request.POST.get('Name')
        data.Address=request.POST.get('Address')
        data.Mobile1=request.POST.get('MobileNo1')
        data.Mobile2=request.POST.get('MobileNo2')
        data.Remarks=request.POST.get('Remarks')
        data.save()
        return redirect('/Labour')
    return render(request,'editlabour.html',{'data':data})

@login_required(login_url='Login')
def DeleteLabour(request,id):
    data=LabourModel.objects.get(id=id)
    data.delete()
    return redirect('/Labour')

@login_required(login_url='Login')
def Rate(request):
    data=RateModel.objects.all()
    return render(request,'rate.html',{'data':data})

@login_required(login_url='Login')
def AddRate(request):
    data=GSTModel.objects.all()
    if request.method=="POST":    
        CodeNo=request.POST.get('CodeNo')
        Description=request.POST.get('Description')
        HSNCode=request.POST.get('HSNCode')
        Unit=request.POST.get('Unit')
        Rate=request.POST.get('Rate')
        Remarks=request.POST.get('Remarks')
        GSTName=request.POST.get('GSTName')
        data=GSTModel.objects.get(GSTName=GSTName)
        SGST=data.SGST
        CGST=data.CGST    
        IGSTName=request.POST.get('IGSTName')
        IGST=0
        dt=RateModel.objects.create(CodeNo=CodeNo,Description=Description,HSNCode=HSNCode,Unit=Unit,Rate=Rate,Remarks=Remarks,GSTName=GSTName,SGST=SGST,CGST=CGST,IGSTName=IGSTName,IGST=IGST)
        dt.save()
        return redirect('/Rate')
    return render(request,'addrate.html',{'data':data})

@login_required(login_url='Login')
def EditRate(request,id):
    gst=GSTModel.objects.all()
    data=RateModel.objects.get(id=id)
    if request.method=="POST":    
        data.CodeNo=request.POST.get('CodeNo')
        data.Description=request.POST.get('Description')
        data.HSNCode=request.POST.get('HSNCode')
        data.Unit=request.POST.get('Unit')
        data.Rate=request.POST.get('Rate')
        data.Remarks=request.POST.get('Remarks')
        GSTName=request.POST.get('GSTName')
        data.GSTName=GSTName
        dt=GSTModel.objects.get(GSTName=GSTName)
        data.SGST=dt.SGST
        data.CGST=dt.CGST    
        data.IGSTName=request.POST.get('IGSTName')
        data.IGST=0
        data.save()
        return redirect('/Rate')
    return render(request,'editrate.html',{'data':data,'gst':gst})

@login_required(login_url='Login')
def DeleteRate(request,id):
    data=RateModel.objects.get(id=id)
    data.delete()
    return redirect('/Rate')

@login_required(login_url='Login')
def Invoice(request):
    return render(request,'invoice.html')

@login_required(login_url='Login')
def AddInvoice(request):
    return render(request,'addinvoice.html')