import sys
import chilkat

#  Note: Requires Chilkat v9.5.0.65 or greater.

#  This requires the Chilkat API to have been previously unlocked.
#  See Global Unlock Sample for sample code.

#  --------------------------------------------------------------------------
#  Create a Shared Access Signature (SAS) token for an Azure Storage Account.
#  --------------------------------------------------------------------------

#  See https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/constructing-an-account-sas
#  for details regarding the Azure Storage Account SAS fields.

authSas = chilkat.CkAuthAzureSAS()
authSas.put_AccessKey("AZURE_ACCESS_KEY")

#  Specify the format of the string to sign.
#  Each comma character in the following string represents a LF ("\n") character.
#  The names specified in the StringToSign are replaced with the values specified
#  in the subsequent calls to SetTokenParam and SetNonTokenParam,.

#  Note: The trailing comma in the StringToSign is intentional and important. This indicates that the
#  string to sign will end with a "\n".

#  Also note: The names in the StringToSign are case sensitive.  The names
#  specified in the 1st argument in the calls to SetNonTokenParam and SetTokenParam should
#  match a name listed in StringToSign.
authSas.put_StringToSign("accountname,signedpermissions,signedservice,signedresourcetype,signedstart,signedexpiry,signedIP,signedProtocol,signedversion,")

#   The account name is "chilkat".  Use your own account name instead of "chilkat".
#   Also use your own container name instead of "mycontainer".
authSas.SetNonTokenParam("accountname","chilkat")

authSas.SetTokenParam("signedpermissions","sp","rwdlacup")
authSas.SetTokenParam("signedservice","ss","bfqt")
authSas.SetTokenParam("signedresourcetype","srt","sco")

dt = chilkat.CkDateTime()
dt.SetFromCurrentSystemTime()
authSas.SetTokenParam("signedstart","st",dt.getAsIso8601("YYYY-MM-DDThh:mmTZD",False))

#  This SAS token will be valid for 30 days.
dt.AddDays(30)
authSas.SetTokenParam("signedexpiry","se",dt.getAsIso8601("YYYY-MM-DDThh:mmTZD",False))

authSas.SetTokenParam("signedProtocol","spr","https")

#   Specifiy values and query param names for each field.
#   If a field is not specified, then an empty string will be used for its value.
authSas.SetTokenParam("signedversion","sv","2015-04-05")

#  Note that we did not call SetTokenParam for "signedIP".  For any omitted fields
#  the value will default to the empty string.

#  Generate the SAS token.
sasToken = authSas.generateToken()
if (authSas.get_LastMethodSuccess() != True):
    print(authSas.lastErrorText())
    sys.exit()

print("SAS token: " + sasToken)

#  Save the SAS token to a file.
#  We can then use this pre-generated token for future Azure Storage Account operations.
fac = chilkat.CkFileAccess()
fac.WriteEntireTextFile("qa_data/tokens/azureStorageAccountSas.txt",sasToken,"utf-8",False)
