# like we donk know what the paitent or hospital will upload as doc. file the prescription might contain medications , amount, disease name or might only conatin any one, any two or might be in some different format, so this will help to structure hte data format..

def build_unified_claim(ocr_data):
    claim = {
        "patient_name": ocr_data.get("patient_name"),
        "disease": None,
        "medications": [],
        "amount": None,
        "has_prescription": False,
        "has_billing": False
    }

    # disease extraction from OCR
    if "diagnosis" in ocr_data and ocr_data["diagnosis"]:
        claim["disease"] = ocr_data["diagnosis"][0]
        claim["has_prescription"] = True

    # type of medication check, whether prescrived or not,...
    if "medications" in ocr_data:
        claim["medications"] = [m["name"] for m in ocr_data["medications"]]
        claim["has_prescription"] = True

    # billing amount chocker
    if "total_amount" in ocr_data and ocr_data["total_amount"]:
        claim["amount"] = ocr_data["total_amount"].get("total_billed")
        claim["has_billing"] = True

    return claim