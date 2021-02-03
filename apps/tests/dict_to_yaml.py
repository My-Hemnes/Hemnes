# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import json, yaml
a = """<Rule '/api/dcmtools/user-series/detection' (POST, OPTIONS) -> dcmtools.UserSeriesDetection>,
 <Rule '/api/pubpools/detections/priorities' (POST, OPTIONS) -> pubpools.PubpoolsPriorities>,
 <Rule '/api/payments/coupons/activities' (PUT, GET, HEAD, POST, OPTIONS) -> payments.CouponActivity>,
 <Rule '/api/payments/orders/verification' (POST, OPTIONS) -> payments.ConsultVerification>,
 <Rule '/api/payments/echo/wechat' (POST, OPTIONS) -> payments.EchoPayWechat>,
 <Rule '/api/informs/admin/inbox' (POST, HEAD, GET, OPTIONS) -> inform.AdminNoticeView>,
 <Rule '/api/examine/auth/order' (POST, OPTIONS) -> examine.UserExaminesAuthOrder>,
 <Rule '/api/wechat/third/oauth' (HEAD, GET, OPTIONS) -> wechat.ThirdOAuthWechatView>,
 <Rule '/api/questionnaire/extensions' (DELETE, HEAD, GET, OPTIONS) -> questionnaire.QuestionExtensions>,
 <Rule '/api/questionnaire/extension' (POST, OPTIONS) -> questionnaire.QuestionnaireExtension>,
 <Rule '/api/questionnaire/feedback' (POST, HEAD, GET, OPTIONS) -> questionnaire.QuestionnaireFeedback>,
 <Rule '/api/notifications/captcha' (POST, PUT, OPTIONS) -> notifications.CaptchaView>,
 <Rule '/api/questionnaire/counts' (HEAD, GET, OPTIONS) -> questionnaire.CountView>,
 <Rule '/api/associations/follows' (PUT, GET, HEAD, POST, OPTIONS) -> associations.AssociationFollows>,
 <Rule '/api/associations/plan' (POST, HEAD, GET, OPTIONS) -> associations.AssociationPlan>,
 <Rule '/api/collections/labels' (POST, HEAD, GET, OPTIONS) -> collections.CollectionLabelView>,
 <Rule '/api/statistics/reports-enumeration' (POST, OPTIONS) -> statistics.ReportsEnumeration>,
 <Rule '/api/statistics/detection-summary' (HEAD, GET, OPTIONS) -> statistics.DetectionSummary>,
 <Rule '/api/statistics/mseries-summary' (HEAD, GET, OPTIONS) -> statistics.MseriesSummary>,
 <Rule '/api/statistics/follows-summary' (HEAD, GET, OPTIONS) -> statistics.FollowsSummary>,
 <Rule '/api/statistics/reports-summary' (HEAD, GET, OPTIONS) -> statistics.ReportsSummary>,
 <Rule '/api/detections/configurations' (PUT, GET, HEAD, POST, OPTIONS) -> detections.ConfigurationView>,
 <Rule '/api/statistics/store-summary' (HEAD, GET, OPTIONS) -> statistics.StoreSummary>,
 <Rule '/api/detections/cooperations' (POST, OPTIONS) -> detections.CooperationsView>,
 <Rule '/api/detections/institutions' (POST, HEAD, GET, OPTIONS) -> detections.InstitutionView>,
 <Rule '/api/detections/custom-conf' (HEAD, PUT, GET, OPTIONS) -> detections.CustomConfView>,
 <Rule '/api/detections/statistics' (POST, OPTIONS) -> detections.DetectStatistics>,
 <Rule '/api/rtempletes/statistics' (PUT, OPTIONS) -> rtempletes.DetectStatistics>,
 <Rule '/api/detections/summaries' (POST, HEAD, GET, OPTIONS) -> detections.SummariesView>,
 <Rule '/api/detections/viewimage' (POST, OPTIONS) -> detections.DetectionViewImage>,
 <Rule '/api/rtempletes/dicomsr' (POST, HEAD, GET, OPTIONS) -> rtempletes.RTempletesDicomSR>,
 <Rule '/api/detections/batch' (POST, OPTIONS) -> detections.BatchDetections>,
 <Rule '/api/followups/coords-summary' (POST, OPTIONS) -> followups.FollowCoords>,
 <Rule '/api/programme/recharge' (PUT, GET, HEAD, POST, OPTIONS) -> programme.CountSchemeTopUp>,
 <Rule '/api/programme/expense' (PUT, OPTIONS) -> programme.CountSchemeExpenseView>,
 <Rule '/api/dcmtools/user-series' (HEAD, GET, OPTIONS) -> dcmtools.DcmtoolUserSeries>,
 <Rule '/api/payments/balances' (HEAD, GET, OPTIONS) -> payments.PayBalances>,
 <Rule '/api/payments/cashouts' (POST, HEAD, GET, OPTIONS) -> payments.PayCashouts>,
 <Rule '/api/dcmtools/followup' (POST, HEAD, GET, OPTIONS) -> dcmtools.DcmtoolPacsFollowup>,
 <Rule '/api/dcmtools/movescu' (POST, OPTIONS) -> dcmtools.DcmtoolPacsMove>,
 <Rule '/api/dcmtools/findscu' (POST, HEAD, GET, OPTIONS) -> dcmtools.DcmtoolPacsFind>,
 <Rule '/api/payments/prices' (POST, HEAD, GET, OPTIONS) -> payments.PriceStrategies>,
 <Rule '/api/payments/orders' (POST, HEAD, GET, OPTIONS) -> payments.Consultations>,
 <Rule '/api/payments/plans' (POST, HEAD, GET, OPTIONS) -> payments.PriceCombination>,
 <Rule '/api/examine/verification' (HEAD, GET, OPTIONS) -> examine.UserExaminesVerification>,
 <Rule '/api/examine/assessment' (HEAD, GET, OPTIONS) -> examine.UserExaminesAssessment>,
 <Rule '/api/examine/detections' (HEAD, GET, OPTIONS) -> examine.UserExaminesDetections>,
 <Rule '/api/billing/expenses' (HEAD, GET, OPTIONS) -> billing.BillExpenses>,
 <Rule '/api/billing/prices' (HEAD, GET, OPTIONS) -> billing.BillPrices>,
 <Rule '/api/examine/synch' (POST, OPTIONS) -> examine.UserExaminesSynch>,
 <Rule '/api/informs/inbox' (PUT, GET, DELETE, HEAD, OPTIONS) -> inform.UserNoticeView>,
 <Rule '/api/billing/plans' (PUT, GET, DELETE, HEAD, POST, OPTIONS) -> billing.BillPlans>,
 <Rule '/api/billing/quota' (PUT, GET, HEAD, POST, OPTIONS) -> billing.BillQuota>,
 <Rule '/api/wechat/signature' (POST, OPTIONS) -> wechat.WechatAuthorization>,
 <Rule '/api/admins/orders' (HEAD, GET, OPTIONS) -> admins.AuthorityOrders>,
 <Rule '/api/wechat/oauth' (HEAD, GET, OPTIONS) -> wechat.OAuthWechatView>,
 <Rule '/api/wechat/echo' (POST, HEAD, GET, OPTIONS) -> wechat.EchoWechatView>,
 <Rule '/api/admins/logs' (HEAD, GET, OPTIONS) -> admins.AuthorityLogs>,
 <Rule '/api/users/thr_reg_fab' (POST, OPTIONS) -> users.UserThrFab>,
 <Rule '/api/store/directories' (PUT, GET, HEAD, POST, OPTIONS) -> store.StoreDirectoriesView>,
 <Rule '/api/store/histories' (DELETE, HEAD, GET, OPTIONS) -> store.StoreHistoryView>,
 <Rule '/api/users/checks' (POST, OPTIONS) -> users.UserApprove>,
 <Rule '/api/store/usages' (HEAD, GET, OPTIONS) -> store.StoreMemoryView>,
 <Rule '/api/users/init' (POST, OPTIONS) -> users.UserInit>,
 <Rule '/api/questionnaire' (POST, HEAD, GET, OPTIONS) -> questionnaire.QuestionnairesView>,
 <Rule '/api/detections' (GET, DELETE, HEAD, POST, OPTIONS) -> detections.Detection>,
 <Rule '/api/rtempletes' (POST, HEAD, GET, OPTIONS) -> rtempletes.RTempletes>,
 <Rule '/api/programme' (HEAD, GET, OPTIONS) -> programme.CountSchemeInformationView>,
 <Rule '/api/followups' (POST, HEAD, GET, OPTIONS) -> followups.Followup>,
 <Rule '/api/pubpools' (POST, OPTIONS) -> pubpools.Pubpools>,
 <Rule '/api/examine' (POST, HEAD, GET, OPTIONS) -> examine.UserExamines>,
 <Rule '/api/admins' (POST, HEAD, GET, OPTIONS) -> admins.AuthorityUserManagement>,
 <Rule '/api/users' (HEAD, GET, OPTIONS) -> users.UserListAuthorization>,
 <Rule '/api/collections/labels/<label_id>/patients/<patient_id>' (HEAD, GET, OPTIONS) -> collections.PatientCollectionView>,
 <Rule '/api/collections/labels/<label_id>/call-off' (DELETE, OPTIONS) -> collections.CancelCollection>,
 <Rule '/api/collections/labels/<label_id>/lesions' (DELETE, OPTIONS) -> collections.LesionCancelCollection>,
 <Rule '/api/detections/institutions/<institute_id>/detail' (HEAD, GET, OPTIONS) -> detections.InstitutionDetail>,
 <Rule '/api/detections/<detect_id>/lesions/calculation' (POST, HEAD, GET, OPTIONS) -> detections.LesionsCalculationView>,
 <Rule '/api/detections/<detect_id>/lesions/manual' (POST, OPTIONS) -> detections.LesionsManualView>,
 <Rule '/api/detections/<detect_id>/lesions/toggle' (PUT, OPTIONS) -> detections.LesionsDisplayStatus>,
 <Rule '/api/detections/<detect_id>/lesions/<lesion_id>/snapshots' (HEAD, GET, OPTIONS) -> detections.LesionPicture>,
 <Rule '/api/detections/<detect_id>/lesions/<lesion_id>/pathology' (PUT, OPTIONS) -> detections.PathologyVerification>,
 <Rule '/api/detections/<detect_id>/report/records/<record_id>' (PUT, GET, DELETE, HEAD, OPTIONS) -> detections.ReportRecordIDView>,
 <Rule '/api/detections/<detect_id>/report/records' (POST, HEAD, GET, OPTIONS) -> detections.ReportRecordView>,
 <Rule '/api/followups/groups/<group_id>/adjustments' (GET, DELETE, HEAD, POST, OPTIONS) -> followups.GroupAdjust>,
 <Rule '/api/pubpools/detections/<detect_id>/reconstructions/<object_name>' (HEAD, GET, OPTIONS) -> pubpools.PubpoolsReconstructions>,
 <Rule '/api/pubpools/detections/<products_type>/<detect_id>/lesions' (HEAD, GET, OPTIONS) -> pubpools.PubpoolsDetectionLesions>,
 <Rule '/api/billing/expenses/<bill_product>/count' (HEAD, GET, OPTIONS) -> billing.BillExpensesCount>,
 <Rule '/api/store/<filename>/download/desensitization' (HEAD, GET, OPTIONS) -> store.StoreDesensitizationDownloadView>,
 <Rule '/api/questionnaire/extensions/<source_code>' (HEAD, GET, OPTIONS) -> questionnaire.QuestionnairesThirdExtension>,
 <Rule '/api/questionnaire/extension/<extension_id>' (POST, HEAD, GET, OPTIONS) -> questionnaire.QuestionExtensionId>,
 <Rule '/api/notifications/<username>/captcha' (POST, PUT, OPTIONS) -> notifications.UserCaptchaView>,
 <Rule '/api/associations/follows/<assn_follow_id>' (PUT, GET, DELETE, HEAD, OPTIONS) -> associations.AssociationFollowsID>,
 <Rule '/api/associations/tracks/<assn_track_id>' (PUT, GET, DELETE, HEAD, OPTIONS) -> associations.AssociationTracksID>,
 <Rule '/api/associations/<mseries_id>/patients' (PUT, OPTIONS) -> associations.AssociationPatientsInfo>,
 <Rule '/api/associations/<assn_follow_id>/tracks' (DELETE, HEAD, GET, OPTIONS) -> associations.AssociationTracks>,
 <Rule '/api/collections/labels/<label_id>' (PUT, GET, DELETE, HEAD, OPTIONS) -> collections.CollectionLabelIDlView>,
 <Rule '/api/collections/<detect_id>/lesions/<lesion_id>' (POST, OPTIONS) -> collections.LesionCollectionView>,
 <Rule '/api/detections/cooperations/<detect_id>' (HEAD, GET, OPTIONS) -> detections.CooperationView>,
 <Rule '/api/detections/institutions/<institute_id>' (HEAD, GET, OPTIONS) -> detections.InstitutionIDView>,
 <Rule '/api/rtempletes/dicomsr/<report_id>' (PUT, GET, DELETE, HEAD, POST, OPTIONS) -> rtempletes.RTDicomSRReportID>,
 <Rule '/api/rtempletes/<rtemplete_id>/institution-logos' (PUT, GET, DELETE, HEAD, OPTIONS) -> rtempletes.RTiInstitutionLogosView>,
 <Rule '/api/rtempletes/<rtemplete_id>/institution-codes' (PUT, GET, DELETE, HEAD, OPTIONS) -> rtempletes.RTInstitutionCodesView>,
 <Rule '/api/detections/<detect_id>/suggestions' (HEAD, PUT, GET, OPTIONS) -> detections.MedicalImageSuggestion>,
 <Rule '/api/detections/<job_id>/algorithmic' (POST, OPTIONS) -> detections.algorithmic>,
 <Rule '/api/rtempletes/<rtemplete_id>/signatures' (PUT, GET, DELETE, HEAD, OPTIONS) -> rtempletes.RTSignatureView>,
 <Rule '/api/detections/<detect_id>/features' (POST, HEAD, GET, OPTIONS) -> detections.DetectFeatures>,
 <Rule '/api/detections/<mseries_id>/patients' (GET, DELETE, HEAD, POST, OPTIONS) -> detections.DetectionPatientsInfo>,
 <Rule '/api/detections/<detect_id>/lesions/<lesion_id>' (PUT, GET, DELETE, HEAD, OPTIONS) -> detections.LesionID>,
 <Rule '/api/detections/<detect_id>/lesions' (POST, HEAD, GET, OPTIONS) -> detections.Lesions>,
 <Rule '/api/detections/<detect_id>/results' (POST, OPTIONS) -> detections.DetectionResultPushView>,
 <Rule '/api/detections/<detect_id>/report' (PUT, GET, DELETE, HEAD, POST, OPTIONS) -> detections.Reports>,
 <Rule '/api/rtempletes/<rtemplete_id>/pdf' (POST, OPTIONS) -> rtempletes.RTempletePDF>,
 <Rule '/api/followups/groups/<group_id>' (HEAD, GET, OPTIONS) -> followups.FollowupGroupID>,
 <Rule '/api/followups/<followup_id>/adjustments' (HEAD, GET, OPTIONS) -> followups.FollowupAdjust>,
 <Rule '/api/followups/<followup_id>/contrast/<contrast_id>' (POST, OPTIONS) -> followups.FollowupUserContrast>,
 <Rule '/api/followups/<followup_id>/contrast' (POST, OPTIONS) -> followups.FollowupContrast>,
 <Rule '/api/programme/<measure_id>/backout' (PUT, OPTIONS) -> programme.CountSchemeBackOut>,
 <Rule '/api/followups/<followup_id>/report' (PUT, GET, DELETE, HEAD, POST, OPTIONS) -> followups.FollowReports>,
 <Rule '/api/pubpools/detections/<products_type>/<detect_id>' (HEAD, GET, OPTIONS) -> pubpools.PubpoolsDetectionID>,
 <Rule '/api/pubpools/detections/<products_type>' (HEAD, GET, OPTIONS) -> pubpools.PubpoolsDetection>,
 <Rule '/api/payments/coupons/<coupon_number>' (PUT, GET, HEAD, POST, OPTIONS) -> payments.CouponCards>,
 <Rule '/api/payments/orders/<order_id>' (PUT, GET, DELETE, HEAD, POST, OPTIONS) -> payments.Consultation>,
 <Rule '/api/examine/detections/<detect_id>' (POST, HEAD, GET, OPTIONS) -> examine.UserExaminesExpertise>,
 <Rule '/api/billing/prices/<price_id>' (DELETE, PUT, OPTIONS) -> billing.BillPricesID>,
 <Rule '/api/informs/inbox/<notice_id>' (DELETE, HEAD, GET, OPTIONS) -> inform.UserNoticeIDView>,
 <Rule '/api/billing/quota/<bill_product>' (PUT, OPTIONS) -> billing.BillQuotaSpend>,
 <Rule '/api/examine/info/<store_id>' (HEAD, GET, OPTIONS) -> examine.UserExamineInfo>,
 <Rule '/api/examine/<filename>/upload' (PUT, OPTIONS) -> examine.UserExaminesAuthUpload>,
 <Rule '/api/admins/<user_id_ordinary>/statistics' (HEAD, GET, OPTIONS) -> admins.AuthorityStatistics>,
 <Rule '/api/admins/<admin_name>/logout' (DELETE, OPTIONS) -> admins.AdminLogout>,
 <Rule '/api/admins/<admin_name>/login' (POST, OPTIONS) -> admins.AdminLogin>,
 <Rule '/api/store/histories/<history_id>' (DELETE, PUT, OPTIONS) -> store.StoreHistoryIDView>,
 <Rule '/api/users/keys/<key>' (DELETE, OPTIONS) -> users.KeySecret>,
 <Rule '/api/store/<filename>/signature' (PUT, GET, DELETE, HEAD, OPTIONS) -> store.StoreSignatureView>,
 <Rule '/api/store/<filename>/download' (POST, HEAD, GET, OPTIONS) -> store.StoreDownloadView>,
 <Rule '/api/store/<filename>/pictures' (PUT, GET, HEAD, POST, OPTIONS) -> store.StorePicturesView>,
 <Rule '/api/users/<username>/logout' (DELETE, OPTIONS) -> users.UserLogout>,
 <Rule '/api/store/<filename>/upload' (PUT, GET, HEAD, POST, OPTIONS) -> store.StoreUploadView>,
 <Rule '/api/users/<username>/reset' (PUT, OPTIONS) -> users.UserRenewal>,
 <Rule '/api/users/<username>/login' (POST, OPTIONS) -> users.UserLogin>,
 <Rule '/api/users/<username>/keys' (POST, HEAD, GET, OPTIONS) -> users.UserKeySecret>,
 <Rule '/api/echo/hello1/<username>' (HEAD, GET, OPTIONS) -> echo.EchoHelloView1>,
 <Rule '/api/echo/hello/<username>' (PUT, GET, DELETE, HEAD, POST, OPTIONS) -> echo.EchoHelloView>,
 <Rule '/api/questionnaire/<chest_id>' (PUT, GET, DELETE, HEAD, OPTIONS) -> questionnaire.QuestionnaireView>,
 <Rule '/api/collections/<detect_id>' (POST, PUT, OPTIONS) -> collections.DetectCollectionView>,
 <Rule '/api/detections/<detect_id>' (PUT, GET, DELETE, HEAD, OPTIONS) -> detections.DetectionID>,
 <Rule '/api/rtempletes/<rtemplete_id>' (PUT, GET, DELETE, HEAD, POST, OPTIONS) -> rtempletes.RTempletesID>,
 <Rule '/api/followups/<followup_id>' (GET, DELETE, HEAD, POST, OPTIONS) -> followups.FollowupID>,
 <Rule '/api/examine/<store_id>' (POST, HEAD, GET, OPTIONS) -> examine.UserExamineDicom>,
 <Rule '/api/admins/<user_id_ordinary>' (POST, HEAD, GET, OPTIONS) -> admins.AuthorityPatientManagement>,
 <Rule '/api/users/<username>' (POST, OPTIONS) -> users.UserUnauthorization>,
 <Rule '/api/users/<username>' (PUT, GET, DELETE, HEAD, OPTIONS) -> users.UserAuthorization>,
 <Rule '/api/store/<filename>' (HEAD, PUT, GET, OPTIONS) -> store.StoreDataView>,
 <Rule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>"""

a_list = a.split("->")

print(a_list)

b_list = list()
for item in a_list:

    b_list.append(item.split(" "))
# print(b_list)

spec = b_list.pop(0)
# print(spec)
b_list.pop(-1)

c_list = list()
for b_item in b_list:
    c_list.append(b_item[3:-1])
c_list.append(spec[1:-1])
print(c_list)


def trans_item(item):
    a = [x.strip("(") for x in item]
    b = [x.strip(")") for x in a]
    c = [x.strip(",") for x in b]
    return c


def trans_str(item):
    return item.strip("'")


data = {"DETECTION": list()}

print(len(c_list))
for c_item in c_list:
    transform_1 = trans_str(c_item[0])
    transform_2 = trans_item(c_item[1::])
    if "OPTIONS" in transform_2:
        transform_2.remove("OPTIONS")
    # print(transform_1, transform_2)
    message = {"display_name": "", "perm_type": "default", "url": str(transform_1), "methods": list(transform_2)}
    data["DETECTION"].append(message)

print(data)

data_str = json.dumps(data)
data_yaml = yaml.safe_load(data_str)

with open("/home/dntech/桌面/detect.yaml", "w", encoding="utf-8") as wy:
    yaml.safe_dump(data_yaml, wy)
