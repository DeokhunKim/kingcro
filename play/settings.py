from capture.object import Object

resolution = (480, 800)
wait_key_interval: int = 1000
waiting_checker_limit: float = 0.965
mouse_interval: float = 0.2

object_entry = [
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/evan_1.png', 'ev1', 0.20, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/evan_2.png', 'ev2', 0.20, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/evan_3.png', 'ev3', 0.20, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/evan_4.png', 'ev4', 0.20, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/evan_5.png', 'ev5', 0.20, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/evan_6.png', 'ev6', 0.20, (0,0)),

    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/armor_1.png', 'am1', 0.15, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/bow_1.png', 'bw1', 0.30, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/bow_3.png', 'bw3', 0.30, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/wand_1.png', 'wd1', 0.30, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/wand_4.png', 'wd4', 0.30, (0,0)),

    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/aramis.png', 'am', 0.20, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/daniel.png', 'dn', 0.20, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/freia.png', 'fa', 0.20, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/leonhard.png', 'lh', 0.20, (0,0)),
    #Object('/Users/thekoon/IntelliJ/_project/kingcro/capture/tune/newevan/shellda.png', 'sd', 0.20, (0,0)),

]

object_stage = [
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/stage/stage_devil.png', 'devil', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/stage/stage_reforge.png', 'reforge', 0.10, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/stage/stage_trader.png', 'trader', 0.10, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/stage/start_btn_1.png', 'start1', 0.10, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/stage/start_btn_2.png', 'start2', 0.10, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/stage/stage_end.png', 'end', 0.10, (0,0)),
]

object_devil_item = [
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/devil_book_3.png', 'book3', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/devil_silver_10.png', 'silver10', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/devil_silver_20.png', 'silver20', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/devil_wand_3.png', 'wand3', 0.13, (0,0)),
]

object_reforge_item = [
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/reforge_armor_1.png', 'armor1', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/reforge_armor_2.png', 'armor2', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/reforge_book_2.png', 'book2', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/reforge_bow_1.png', 'bow1', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/reforge_bow_2.png', 'bow2', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/reforge_expand.png', 'expand', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/reforge_medal.png', 'medal', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/reforge_sword_1.png', 'sword1', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/reforge_sword_2.png', 'sword2', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/reforge_wand_2.png', 'wand2', 0.13, (0,0)),
]

object_trader_item = [
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/trader_armor_1.png', 'armor1', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/trader_bow_1.png', 'bow1', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/trader_bow_2.png', 'bow2', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/trader_medal.png', 'medal', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/trader_summon_1.png', 'summon1', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/trader_sword_1.png', 'sword1', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/trader_sword_2.png', 'sword2', 0.13, (0,0)),
    Object('/Users/thekoon/IntelliJ/_project/kingcro/play/template_img/item/trader_wand_1.png', 'wand1', 0.18, (0,0)),
]