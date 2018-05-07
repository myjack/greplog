# -*- coding: utf-8 -*-



import difflib



s1 = '2018-03-28 15:54:57,944 ERROR com.linkage.lcsmp.pdmanage.sms.dao.impl.IsmsusertelDAOImpl  -> 获取用户手机信息失'

s2 = '2018-03-28 05:50:49,443 ERROR com.linkage.lcsmp.pdmanage.charging.dao.impl.ChargingDAOImpl  -> 查询所有计费策略信息失败！'

print('s1 = ', s1)

print('s2 = ', s2)

print('s1 == s2', s1 == s2)

print('')


matcher = difflib.SequenceMatcher(None, s1, s2)

print(matcher)

print('ratio():', matcher.ratio())

print('quick_ratio():', matcher.quick_ratio())

print('real_quick_ratio():', matcher.real_quick_ratio())
