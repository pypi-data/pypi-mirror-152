var DurationTime = .25,
	RPTop, RPLeft, RPRight, RPBottom, RPCenter, RPOut = [],
	DealLogScene;
window.onorientationchange = function() {
	location.reload()
};
window.onload = function() {
	document.title = Request.str;
	cc.game.onStart = function() {
		cc.LoaderScene.preload(["Bids.png", "Cards.png", "CardBack.png", "BoxBid.png", "BoxPlay.png", "ButL.png", "ButR.png", ], function() {
			var n = window.innerWidth / window.innerHeight,
				t = n < 4 / 5 ? cc.ResolutionPolicy.FIXED_WIDTH : cc.ResolutionPolicy.SHOW_ALL;
			cc.view.adjustViewPort(!0);
            cc.view.enableAutoFullScreen(false);
			cc.view.setDesignResolutionSize(640, 960, t);
			cc.view.resizeWithBrowserSize(!0);
			cc.director.runScene(new DealLogScene);
			document.getElementById("gameCanvas").style.visibility = ""
		}, this)
	};
	document.getElementById("gameCanvas").style.visibility = "hidden";
	cc.game.run("gameCanvas")
};
DealLogScene = cc.Scene.extend({
	butLastSprite: null,
	butNextSprite: null,
	boxBidSprite: null,
	boxPlaySprite: null,
	playerSit: Direction.NoDirection,
	dealer: Direction.NoDirection,
	vul: Vulnerability.None,
	declarer: Direction.NoDirection,
	contract: null,
	winTrick: 0,
	playIndex: 0,
	playList: [],
	leadList: [],
	wintList: [],
	hands: [],
	seatLabel: [],
	winBLabel: null,
	winDLabel: null,
	maxTrick: 0,
	onEnter: function() {
		var n, t;
		this._super();
		n = cc.director.getWinSize();
		RPTop = cc.p(n.width / 2, n.height - 80);
		RPLeft = cc.p(0, n.height / 2);
		RPRight = cc.p(n.width, n.height / 2);
		RPBottom = cc.p(n.width / 2, 80);
		RPCenter = cc.p(n.width / 2, n.height / 2);
		RPOut[0] = cc.p(RPCenter.x, RPCenter.y - 32);
		RPOut[1] = cc.p(RPCenter.x - 32, RPCenter.y);
		RPOut[2] = cc.p(RPCenter.x, RPCenter.y + 32);
		RPOut[3] = cc.p(RPCenter.x + 32, RPCenter.y);
		t = cc.LayerColor.create(cc.color(40, 61, 5, 255), n.width, n.height);
		this.addChild(t);
		this.butLastSprite = new cc.Sprite("ButL.png");
		this.butLastSprite.setPosition(60, 78);
		this.addChild(this.butLastSprite);
		this.butNextSprite = new cc.Sprite("ButR.png");
		this.butNextSprite.setPosition(580, 78); 
        this.addChild(this.butNextSprite);
		cc.eventManager.addListener({
			event: cc.EventListener.TOUCH_ONE_BY_ONE,
			swallowTouches: !0,
			onTouchBegan: function(n, t) {
				var i = t.getCurrentTarget(),
					r = i.convertToNodeSpace(n.getLocation());
				i.onTouch(r);
				return !0
			}
		}, this);
		this.playerSit = Direction.South;
		this.dealer = ProtocolCodec.DirectionFromString(Request.dealer);
		this.vul = ProtocolCodec.VulnerabilityFromString(Request.vul);
		this.declarer = ProtocolCodec.DirectionFromString(Request.declarer);
		this.contract = ProtocolCodec.ContractFromString(Request.contract);
		this.winTrick = Request.wintrick;
		this.initContorls();
		this.processHandData();
		this.processBidLog();
		this.processPlayLog();
		this.sortAllHands();
		this.placeAllHands();
		this.winTrick = 0;
		this.updateWinTrick();
		this.playIndex = 0;
		this.boxPlaySprite.setVisible(!1);
		this.butLastSprite.setVisible(!1);
		this.butNextSprite.setVisible(this.contract.getType() != BidType.NotContract)
	},
	initContorls: function() {
		var t, i, r, n, f, u, e;
		for(this.boxBidSprite = cc.Sprite.create("BoxBid.png", cc.rect((this.vul & 1) * 320, (this.vul >> 1) * 408, 320, 408)), this.boxBidSprite.setPosition(RPCenter), this.addChild(this.boxBidSprite), this.boxPlaySprite = cc.Sprite.create("BoxPlay.png"), this.boxPlaySprite.setPosition(RPCenter), this.addChild(this.boxPlaySprite), t = ["SOUTH", "WEST", "NORTH", "EAST"], this.seatLabel[0] = cc.LabelTTF.create(t[0], "Arial", 22), this.seatLabel[0].setPosition(230, 106), this.seatLabel[0].setRotation(0), this.boxPlaySprite.addChild(this.seatLabel[0]), this.seatLabel[1] = cc.LabelTTF.create(t[1], "Arial", 22), this.seatLabel[1].setPosition(76, 264), this.seatLabel[1].setRotation(270), this.boxPlaySprite.addChild(this.seatLabel[1]), this.seatLabel[2] = cc.LabelTTF.create(t[2], "Arial", 22), this.seatLabel[2].setPosition(230, 420), this.seatLabel[2].setRotation(0), this.boxPlaySprite.addChild(this.seatLabel[2]), this.seatLabel[3] = cc.LabelTTF.create(t[3], "Arial", 22), this.seatLabel[3].setPosition(384, 264), this.seatLabel[3].setRotation(90), this.boxPlaySprite.addChild(this.seatLabel[3]), this.winBLabel = cc.LabelTTF.create("", "Arial", 24), this.winBLabel.setPosition(230, 120), this.winBLabel.setDimensions(300, 40), this.winBLabel.setHorizontalAlignment(cc.TEXT_ALIGNMENT_LEFT), this.boxPlaySprite.addChild(this.winBLabel), this.winDLabel = cc.LabelTTF.create("", "Arial", 24), this.winDLabel.setPosition(230, 120), this.winDLabel.setDimensions(300, 40), this.winDLabel.setHorizontalAlignment(cc.TEXT_ALIGNMENT_RIGHT), this.boxPlaySprite.addChild(this.winDLabel), i = cc.color(252, 99, 99, 255), r = cc.color(208, 255, 148, 255), n = 0; n < 4; n++)
			if(u = DirectionDistance(this.playerSit, n), f = this.seatLabel[u], f.setColor(IsVulnerability(this.vul, n) ? i : r), f.setString(t[n]), n == this.dealer) {
				var o = f.getTextureRect().width,
					s = f.getColor(),
					h = cc.LayerColor.create(s, o, 2);
				f.addChild(h)
			}
		this.declarer % 2 == 0 ? (this.winBLabel.setColor(IsVulnerability(this.vul, Direction.North) ? i : r), this.winDLabel.setColor(IsVulnerability(this.vul, Direction.East) ? i : r)) : (this.winBLabel.setColor(IsVulnerability(this.vul, Direction.East) ? i : r), this.winDLabel.setColor(IsVulnerability(this.vul, Direction.North) ? i : r));
		u = DirectionAdd(this.playerSit, this.declarer);
		this.seatLabel[u].setVisible(!1);
		e = GetContractSprite(this.contract);
		e.setPosition(this.seatLabel[u].getPosition());
		e.setRotation(this.seatLabel[u].getRotation());
		e.setScale(.5);
		this.boxPlaySprite.addChild(e)
	},
	onTouch: function(n) {
		this.butNextSprite.isVisible() && cc.rectContainsPoint(this.butNextSprite.boundingBox(), n) ? this.onNext() : this.butLastSprite.isVisible() && cc.rectContainsPoint(this.butLastSprite.boundingBox(), n) && this.onLast()
	},
	onLast: function() {
		var i, r, n, t;
		if(!(this.playIndex <= 0)) {
			if(this.playIndex == this.maxTrick && this.butNextSprite.setVisible(!0), this.playIndex--, this.playIndex == 0) this.boxBidSprite.setVisible(!0), this.boxPlaySprite.setVisible(!1), this.butLastSprite.setVisible(!1), this.winTrick = 0, this.updateWinTrick();
			else {
				for(i = (this.playIndex - 1) * 4, n = 0; n < 4; n++) t = this.playList[i++], t.runAction(cc.FadeIn.create(DurationTime));
				this.winTrick = this.wintList[this.playIndex - 1];
				this.updateWinTrick()
			}
			for(i = this.playIndex * 4, r = DirectionDistance(this.playerSit, this.leadList[this.playIndex]), n = 0; n < 4; n++) t = this.playList[i++], t.setOpacity(255), this.hands[r].push(t), r = DirectionAdd(r, 1);
			this.sortAllHands();
			this.placeAllHands()
		}
	},
	onNext: function() {
		var i, r, n, t, u;
		if(!(this.playIndex >= this.maxTrick)) {
			if(this.playIndex == 0) this.boxBidSprite.setVisible(!1), this.boxPlaySprite.setVisible(!0), this.butLastSprite.setVisible(!0);
			else
				for(i = (this.playIndex - 1) * 4, n = 0; n < 4; n++) t = this.playList[i++], t.runAction(cc.FadeOut.create(DurationTime));
			for(i = this.playIndex * 4, r = DirectionDistance(this.playerSit, this.leadList[this.playIndex]), n = 0; n < 4; n++) {
				u = cc.Sequence.create(cc.DelayTime.create(DurationTime * n), cc.MoveTo.create(DurationTime, RPOut[r]));
				t = this.playList[i++];
				t.stopAllActions();
				t.runAction(u);
				t.setZOrder(i);
				var o = t.getTag(),
					f = this.hands[r];
				for(var e in f)
					if(f[e].getTag() == o) break;
				f.splice(e, 1);
				r = DirectionAdd(r, 1)
			}
			u = cc.Sequence.create(cc.DelayTime.create(DurationTime * 4), cc.CallFunc.create(this.placeAllHands, this), cc.CallFunc.create(this.updateWinTrick, this));
			this.runAction(u);
			this.winTrick = this.wintList[this.playIndex];
			this.playIndex++;
			this.playIndex == this.maxTrick && this.butNextSprite.setVisible(!1)
		}
	},
	processHandData: function() {
		var f = Request.deal.split(" "),
			r, i, t, u, n;
		for(r in f) {
			i = DirectionAdd(this.dealer, r - this.playerSit + 4);
			t = [];
			ProtocolCodec.HandFromString(f[r], t);
			this.hands[i] = [];
			for(u in t) n = GetCardSprite(t[u]), n.setPosition(RPCenter), n.setScale(.5), n.setRotation(90 * i), n.setTag(t[u].getIndex()), this.hands[i].push(n), this.addChild(n)
		}
	},
	processBidLog: function() {
		var t = [],
			n, i, u;
		ProtocolCodec.BidLogFromString(Request.bidlog, t);
		n = this.dealer;
		i = 300 / Math.ceil((n + t.length) / 4);
		i > 50 && (i = 50);
		for(u in t) {
			var f = n & 3,
				e = n >> 2,
				r = GetBidSprite(t[u]);
			r.setPositionX(40 + f * 80);
			r.setPositionY(320 - e * i);
			r.setScale(.5);
			this.boxBidSprite.addChild(r);
			n++
		}
	},
	processPlayLog: function() {
		var r = [],
			u, n, t, i;
		for(ProtocolCodec.PlayLogFromString(Request.playlog, r, this.leadList), this.maxTrick = Math.floor(r.length / 4), u = 0, n = 0; n < this.maxTrick; n++) {
			for(t = DirectionDistance(this.playerSit, this.leadList[n]), i = 0; i < 4; i++) {
				var o = r[n * 4 + i].getIndex(),
					f = this.hands[t];
				for(var e in f)
					if(f[e].getTag() == o) break;
				this.playList.push(f[e]);
				t = DirectionAdd(t, 1)
			}
			n > 0 && (DirectionDistance(this.declarer, this.leadList[n]) % 2 == 0 && u++, this.wintList.push(u))
		}
		this.wintList.push(this.winTrick)
	},
	placeCardsToBottomLine: function(n) {
		for(var i, r, u = n.length, f = RPBottom.x - (u - 1) * 12, e = RPBottom.y, t = 0; t < u; t++) i = n[t], r = cc.MoveTo.create(DurationTime / 2, cc.p(f, e)), i.stopAllActions(r), i.runAction(r), f += 24
	},
	placeCardsToTopLine: function(n) {
		for(var i, r, u = n.length, f = RPTop.x - (u - 1) * 12, e = RPTop.y, t = 0; t < u; t++) i = n[t], r = cc.MoveTo.create(DurationTime / 2, cc.p(f, e)), i.stopAllActions(r), i.runAction(r), f += 24
	},
	placeCardsToLeftLine: function(n) {
		for(var i, r, u = n.length, e = RPLeft.x, f = RPLeft.y + (u - 1) * 12, t = 0; t < u; t++) i = n[t], r = cc.MoveTo.create(DurationTime / 2, cc.p(e, f)), i.stopAllActions(r), i.runAction(r), f -= 24
	},
	placeCardsToRightLine: function(n) {
		for(var i, r, u = n.length, e = RPRight.x, f = RPRight.y + (u - 1) * 12, t = 0; t < u; t++) i = n[t], r = cc.MoveTo.create(DurationTime / 2, cc.p(e, f)), i.stopAllActions(r), i.runAction(r), f -= 24
	},
	placeAllHands: function() {
		this.placeCardsToBottomLine(this.hands[0]);
		this.placeCardsToLeftLine(this.hands[1]);
		this.placeCardsToTopLine(this.hands[2]);
		this.placeCardsToRightLine(this.hands[3])
	},
	sortAllHands: function() {
		for(var n, r, u, f = this.contract.getType() != BidType.NotContract ? this.contract.getTrump() : SuitValue.NoTrump, i = ProtocolCodec.SuitSortCardsRnk[f], t = 0; t < 4; t++) {
			n = this.hands[t];
			n.sort(function(n, t) {
				var r = new Card,
					u = new Card;
				return r.setIndex(n.getTag()), u.setIndex(t.getTag()), r.getSuit() != u.getSuit() ? i[r.getSuit()] - i[u.getSuit()] : u.getRank() - r.getRank()
			});
			r = 100;
			for(u in n) n[u].setZOrder(r++)
		}
	},
	updateWinTrick: function() {
		var n = this.contract.getRank() + 6,
			t = this.playIndex < this.maxTrick ? this.playIndex : 13;
		this.declarer % 2 == 0 ? (this.winBLabel.setString("NS:" + this.winTrick + "/" + n), this.winDLabel.setString("EW:" + (t - this.winTrick))) : (this.winBLabel.setString("EW:" + this.winTrick + "/" + n), this.winDLabel.setString("NS:" + (t - this.winTrick)))
	}
})